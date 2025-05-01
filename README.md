# Django Sortable List with Drag-and-Drop Ordering

This project demonstrates how to create a sortable list using Django and [SortableJS](https://sortablejs.github.io/Sortable/). Users can drag-and-drop list items to reorder them, and the new order is saved to the database via AJAX.

## Features

- Django backend for storing and updating item order
- SortableJS for drag-and-drop functionality
- AJAX (fetch API) to send the new order without refreshing the page
- CSRF protection

---

## Installation

1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-sortable-list.git
cd django-sortable-list
```

2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install django
```

4. Set Up the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create Test Items (Optional)
```bash
python manage.py shell
```
```python
from items.models import Item
Item.objects.create(name="Item 1")
Item.objects.create(name="Item 2")
Item.objects.create(name="Item 3")
exit()
```

6. Run the Development Server
```bash
python manage.py runserver
```
Then open your browser at: http://127.0.0.1:8000/

## Explanation

Model (models.py)
```python
class Item(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
```

### View Functions (views.py)
- item_list(request) renders the list

- reorder_items(request) handles AJAX post requests and updates the order in the database

### Template (item_list.html)
- Uses SortableJS to enable drag-and-drop

- Sends new item order to the backend via fetch() with the CSRF token

## API Endpoint
- POST /reorder/

- Request:

```json
{
  "order": ["3", "1", "2"]
}
```

- Response:
```json
{
  "status": "success"
}
```

## CSRF Setup
- {% csrf_token %} is used in the HTML

- A hidden input is used to grab the token via JavaScript:
```html
<input type="hidden" id="csrf-token" value="{{ csrf_token }}" />
```
