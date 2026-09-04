"""
Multi-Format Enterprise Report Generator (PDF, CSV, HTML).
"""
import os
import csv
from io import StringIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from ..config.settings import Config
from ..models import Complaint, TrafficRecord, WasteBin, WaterTank, Transformer, PollutionRecord, SystemAlert

class ReportService:
    @staticmethod
    def generate_csv_report(module_name):
        """Generate raw CSV content string for a given smart city module."""
        output = StringIO()
        writer = csv.writer(output)

        if module_name == "complaints":
            writer.writerow(["Ticket Number", "Title", "Category", "Status", "Priority", "Zone", "Created At"])
            records = Complaint.query.limit(500).all()
            for r in records:
                writer.writerow([
                    r.ticket_number, r.title,
                    r.category.name if r.category else "General",
                    r.status, r.priority, r.zone,
                    r.created_at.strftime("%Y-%m-%d %H:%M")
                ])
        elif module_name == "traffic":
            writer.writerow(["Road ID", "Vehicle Count", "Avg Speed (km/h)", "Congestion Level", "Recorded At"])
            records = TrafficRecord.query.limit(500).all()
            for r in records:
                writer.writerow([r.road_id, r.vehicle_count, r.average_speed_kmh, r.congestion_level, r.recorded_at.strftime("%Y-%m-%d %H:%M")])
        else:
            writer.writerow(["Timestamp", "Module", "Description"])
            writer.writerow([datetime.utcnow().isoformat(), module_name, "Summary Report Data"])

        return output.getvalue()

    @staticmethod
    def generate_pdf_report(report_title, data_rows, file_name="city_report.pdf"):
        """Generate formal PDF report using ReportLab."""
        Config.init_dirs()
        file_path = os.path.join(Config.REPORTS_DIR, file_name)
        doc = SimpleDocTemplate(file_path, pagesize=letter)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#1E293B"),
            alignment=1, # Center
            spaceAfter=20
        )

        elements = []
        elements.append(Paragraph(f"<b>Smart City Platform</b>", title_style))
        elements.append(Paragraph(f"<b>{report_title}</b>", styles['Heading2']))
        elements.append(Paragraph(f"Generated on: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}", styles['Normal']))
        elements.append(Spacer(1, 15))

        if data_rows:
            table = Table(data_rows)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0F172A")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ]))
            elements.append(table)
        else:
            elements.append(Paragraph("No records found for the selected criteria.", styles['Italic']))

        doc.build(elements)
        return file_path
