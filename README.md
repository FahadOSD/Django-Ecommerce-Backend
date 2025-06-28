# E-commerce API

A Django REST API for an e-commerce platform with user authentication, product management, shopping cart functionality, and Stripe payment integration.

## 🚀 Features

- **User Authentication**: Registration, login, logout with custom User model
- **Product Management**: CRUD operations for products with categories
- **Shopping Cart**: Add/remove products from cart
- **Payment Integration**: Stripe payment processing
- **Image Storage**: Cloudinary integration for product images
- **API Documentation**: Swagger/OpenAPI documentation
- **Security**: Environment variables for sensitive data

## 🛠️ Tech Stack

- **Backend**: Django 5.0.8
- **API**: Django REST Framework 3.15.2
- **Database**: SQLite (development)
- **Authentication**: Token Authentication
- **Payment**: Stripe
- **Image Storage**: Cloudinary
- **Documentation**: drf-yasg (Swagger)

## 📋 Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd e-commerce-api-final
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file with your actual credentials:
   ```env
   # Cloudinary Configuration
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret

   # Stripe Configuration
   STRIPE_SECRET_KEY=your_stripe_secret_key
   STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
   STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 📚 API Endpoints

### Authentication
- `POST /api/accounts/register/` - User registration
- `POST /api/accounts/login/` - User login
- `POST /api/accounts/logout/` - User logout
- `GET /api/accounts/profile/` - Get user profile

### Categories
- `GET /api/accounts/categories/` - List all categories
- `GET /api/accounts/categories/{id}/` - Get category details

### Products
- `GET /api/accounts/products/` - List all products
- `POST /api/accounts/products/` - Create new product
- `GET /api/accounts/products/{product_tag}/` - Get product details
- `PUT /api/accounts/products/{product_tag}/` - Update product
- `DELETE /api/accounts/products/{product_tag}/` - Delete product

### Cart
- `GET /api/accounts/carts/` - List all carts
- `GET /api/accounts/carts/{id}/` - Get cart details
- `POST /api/accounts/carts/` - Add products to cart

### Users
- `GET /api/accounts/users/` - List all users
- `GET /api/accounts/users/{id}/` - Get user details

### Payment
- `POST /api/payment/create-checkout-session/{product_id}/` - Create Stripe checkout session
- `POST /api/payment/webhook/` - Stripe webhook endpoint

## 🔐 Authentication

The API uses Token Authentication. Include the token in your requests:

```bash
Authorization: Token your_token_here
```

## 📖 API Documentation

Access the interactive API documentation at:
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## 🗄️ Database Models

### User
- Custom User model extending AbstractUser
- Email as username field
- Additional fields: phone, date_of_birth

### Category
- title: CharField

### Product
- product_tag: CharField (Primary Key)
- name: CharField
- category: ForeignKey to Category
- price: IntegerField
- stock: IntegerField
- image: ImageField (Cloudinary)
- created_by: ForeignKey to User
- status: BooleanField
- date_created: DateField

### Cart
- cart_id: OneToOneField to User (Primary Key)
- created_at: DateTimeField
- products: ManyToManyField to Product

### PurchaseHistory
- purchase_id: CharField (UUID)
- product: ForeignKey to Product
- purchase_success: BooleanField
- date: DateTimeField

## 🔧 Configuration

### Environment Variables
All sensitive configuration is stored in environment variables:

- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
- `CLOUDINARY_API_KEY`: Your Cloudinary API key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API secret
- `STRIPE_SECRET_KEY`: Your Stripe secret key
- `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key
- `STRIPE_WEBHOOK_SECRET`: Your Stripe webhook secret

### Django Settings
- `APPEND_SLASH = False`: URLs work with or without trailing slashes
- `AUTH_USER_MODEL = 'accounts.User'`: Custom user model
- `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`: Cloudinary for file storage

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure production database (PostgreSQL recommended)
3. Set up proper environment variables
4. Configure static file serving
5. Set up web server (nginx + gunicorn)

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🤝 Support

For support, please open an issue in the repository or contact the development team.

## 🔗 External Services

- [Stripe](https://stripe.com/) - Payment processing
- [Cloudinary](https://cloudinary.com/) - Image storage and management 