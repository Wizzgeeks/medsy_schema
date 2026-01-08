from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, CASCADE, IntField, DictField
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime, timezone
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year

class Book_upload(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    year = ReferenceField(Year, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    layer1 = ReferenceField(Layer_1, reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2, reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3, reverse_delete_rule=CASCADE)
    uploaded_by = ReferenceField(Admin, required=True, reverse_delete_rule=CASCADE)
    uploaded_at = DateTimeField(default=datetime.now(timezone.utc))
    layer = StringField(choices=['subject', 'layer1', 'layer2', 'layer3'], required=True)
    book_name = StringField(required=True)
    book_url_s3 = StringField(required=True)
    neo4j_id = StringField(required=True)
    active = BooleanField(default=True)
    status = StringField(default="PENDING", choices=["PENDING", "PROCESSING", "COMPLETED", "FAILED"])
    last_processed_page = IntField(default=0)
    total_pages = IntField(default=0)
    error_message = StringField()
    completed_at = DateTimeField(null=True)
    processing_started_at = DateTimeField(null=True)
    meta_data = DictField(default={})
    task_id = StringField()

    meta = {
        'indexes': [
            'status',
            'uploaded_at',
            {'fields': ['status', 'uploaded_by'], 'name': 'status_user_idx'},
            {'fields': ['neo4j_id'], 'unique': True}
        ]
    }

    def to_json(self):
        return {
            'id': str(self.id),
            'course': str(self.course.id) if self.course else None,
            'year': str(self.year.id) if self.year else None,
            'subject': str(self.subject.id) if self.subject else None,
            'layer1': str(self.layer1.id) if self.layer1 else None,
            'layer2': str(self.layer2.id) if self.layer2 else None,
            'layer3': str(self.layer3.id) if self.layer3 else None,
            'uploaded_by': str(self.uploaded_by.id) if self.uploaded_by else None,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'layer': self.layer,
            'book_name': self.book_name,
            'book_url_s3': self.book_url_s3,
            'neo4j_id': self.neo4j_id,
            'active': self.active,
            'status': self.status,
            'last_processed_page': self.last_processed_page,
            'total_pages': self.total_pages,
            'error_message': self.error_message,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'processing_started_at': self.processing_started_at.isoformat() if self.processing_started_at else None,
            'task_id': self.task_id,
            'progress': self.get_progress_percentage()
        }

    def get_progress_percentage(self):
        """Calculate progress percentage"""
        if self.status == "COMPLETED":
            return 100
        elif self.status == "PENDING":
            return 0
        elif self.total_pages > 0 and self.last_processed_page > 0:
            return min(99, int((self.last_processed_page / self.total_pages) * 100))
        elif self.status == "PROCESSING":
            return 10  # Just started
        return 0

    def update_progress(self, current_page, total_pages=None):
        """Update progress of book processing"""
        self.last_processed_page = current_page
        if total_pages:
            self.total_pages = total_pages
        if current_page >= self.total_pages and self.total_pages > 0:
            self.status = "COMPLETED"
            self.completed_at = datetime.now(timezone.utc)
        else:
            self.status = "PROCESSING"
        self.save()

    def mark_failed(self, error_message):
        """Mark book as failed"""
        self.status = "FAILED"
        self.error_message = str(error_message)[:500]
        self.save()

    def mark_processing(self):
        """Mark book as processing"""
        self.status = "PROCESSING"
        self.processing_started_at = datetime.now(timezone.utc)
        self.save()

    def mark_completed(self):
        """Mark book as completed"""
        self.status = "COMPLETED"
        self.completed_at = datetime.now(timezone.utc)
        self.active = True
        self.last_processed_page = self.total_pages if self.total_pages > 0 else 1
        self.save()