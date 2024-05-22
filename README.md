# Rxpress  

 **for quick and easy refills**



Rxpress is an intuitive pharmacy management application aimed at simplifying the prescription process for both patients and pharmacists. It provides a seamless platform for managing prescriptions, allowing patients to conveniently order and track their medications, while enabling pharmacists to efficiently review and process prescription requests.

## Key Features

### For Patients:

- **Prescription Management**: Easily add prescriptions to a digital basket for approval.
- **Real-Time Status Updates**: Receive instant updates on prescription status changes.
- **Basket Functionality**: Manage prescriptions in the digital basket, including adding, removing, or updating quantities.

### For Pharmacists:

- **Pharmacist Dashboard**: Efficiently review and process incoming prescription requests.
- **Prescription Review**: Quickly review patient prescriptions and update their status.
- **Red-Shift Toggle**: Adjust screen colors to reduce eye strain during extended work sessions.


## Backend (Flask, SQLAlchemy, Alembic)

### Models

- **User Model**: Represents both patients and pharmacists.
- **Patient Model**: Represents patients.
- **Pharmacist Model**: Represents pharmacists.
- **Prescription Model**: Represents prescriptions.
- **Basket Model**: Represents the digital basket for patients.

### Routes

- **Prescription Routes**: /prescriptions, /prescriptions/int:id.
- **Basket Routes**: /baskets, /baskets/int:id.

### Alembic Migration

- Initialize Alembic with `flask db init`.
- Create migration scripts with `flask db migrate -m "Initial migration"`.
- Apply migrations with `flask db upgrade`.

## Frontend (React, React Router)

### Routes

- **Dashboard**: /dashboard.
- **Prescriptions**: /prescriptions.
- **Basket**: /basket.

### Components

- **DashboardComponent**
- **PrescriptionListComponent**
- **BasketComponent**

## Stretch Goals

- **Authentication System**: Implement a secure user authentication system for patient and pharmacist logins.
- **Point of Sale (POS) Integration**: Integrate with point-of-sale systems for seamless checkout and inventory management.
- **Medication Refill Reminders**: Send automated reminders to patients for prescription refills.
- **Inventory Management**: Integrate with pharmacy inventory systems for stock level tracking and resupply notifications.
- **Patient Medication History**: Access complete medication history for better prescription decisions.


## Pharmacist Dashboard Structure

### Primary Goals

1. **Patient Search**: Search for patients by name.
2. **Prescription Management**: Review and update prescription status.

### Core Logic

- **State Management**: Track patients, prescriptions, loading states, and errors.
- **Fetch Functions**: Fetch patients and prescriptions from the backend.
- **Event Handlers**: Handle search queries and patient selection.
- **Rendering Logic**: Render patient listings and prescription details dynamically.
