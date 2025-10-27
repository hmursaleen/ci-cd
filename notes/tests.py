from django.test import TestCase

import pytest
from django.utils import timezone
from .models import Note

@pytest.mark.django_db
def test_create_one():
    n = Note.objects.create(title='First', content='hello')
    assert n.pk is not None
    assert n.title == 'First'
    assert n.created_at is not None
