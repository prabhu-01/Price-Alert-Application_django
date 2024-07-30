# Price Alert Application

## Overview

This application allows users to set price alerts for cryptocurrencies. When the target price is reached, an email notification is sent to the user.

## Setup and Running the Project

### Prerequisites

- Docker
- Docker Compose

### Steps to Run the Project

1. Clone the repository.
2. Navigate to the project directory.
3. Build and start the containers:
   ```sh
   docker-compose up --build


**Endpoints**
  User Authentication
    > POST /api/token/ - Obtain JWT token.
    > POST /api/token/refresh/ - Refresh JWT token.

    
**Alerts**
  > POST /alerts/create/ - Create a new alert.
  > DELETE /alerts/delete/<id>/ - Delete an alert.
  > GET /alerts/ - Fetch all alerts (with pagination and filtering).

**Solution for Sending Alerts**
_The application uses Binance's WebSocket for real-time price updates. When a cryptocurrency's price reaches the user's target price, an email is sent to the user._

**Environment Variables**
_DATABASE_URL - PostgreSQL database URL.
REDIS_URL - Redis URL.
EMAIL_HOST - Email host.
EMAIL_PORT - Email port.
EMAIL_HOST_USER - Email host user.
EMAIL_HOST_PASSWORD - Email host password._
