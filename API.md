# Stadium Reservation System API Reference

  

This document provides a comprehensive list of all API endpoints used in the Stadium Reservation application, organized by functional category.

  

## Table of Contents

- [[#Authentication]]

- [[#Stadium Management]]

- [[#Stadium Scheduling]]

- [[#Session Templates]]

- [[#Available Sessions]]

- [[#Bookings]]

- [[#Referee Management]]

- [[#Admin Management]]

- [[#Data Models]]

  

## Authentication

  

> [!info] Base URL

> All authentication endpoints use base URL: `/api/users`

  

| Endpoint | Method | Description | Parameters |

| -------- | ------ | ----------- | ---------- |

| `/login` | `POST` | User login | `email`, `password` |

| `/register` | `POST` | Register new user | `name`, `email`, `phone`, `password`, `user_type` |

| `/me` | `GET` | Get current user profile | - |

| `/logout` | `POST` | Logout user | - |

| `/verify-token` | `GET` | Verify token validity | - |

  

## Stadium Management

  

> [!info] Base URL

> All stadium endpoints use base URL: `/api/stadiums`

  

| Endpoint                  | Method   | Description                          | Parameters                                                                           |
| ------------------------- | -------- | ------------------------------------ | ------------------------------------------------------------------------------------ |
| `/`                       | `GET`    | List all stadiums                    | Optional: `limit`, `page`, `status`, `sport_type`                                    |
| `/`                       | `POST`   | Create a new stadium                 | `name`, `location`, `description`, `sport_type`, `capacity`, `hourly_rate`, `status` |
| `/:id`                    | `GET`    | Get stadium by ID                    | -                                                                                    |
| `/:id`                    | `PATCH`  | Update stadium                       | Any stadium fields                                                                   |
| `/:id`                    | `DELETE` | Delete stadium                       | -                                                                                    |
| `/owner`                  | `GET`    | Get stadiums owned by current user   | -                                                                                    |
| `/:id/available-sessions` | `GET`    | Get available sessions for a stadium | Optional: `date`, `status`                                                           |

## Stadium Scheduling

> [!info] Base URLs
> - Stadium schedules: `/api/stadiums/:stadiumId/day-schedules`
> - Individual day schedules: `/api/day-schedules`

| Endpoint                                      | Method   | Description                             | Parameters                  |
| --------------------------------------------- | -------- | --------------------------------------- | --------------------------- |
| `/api/stadiums/:stadiumId/day-schedules`      | `GET`    | Get all day schedules for a stadium     | -                           |
| `/api/stadiums/:stadiumId/day-schedules`      | `POST`   | Create a day schedule                   | `day_of_week`, `time_slots` |
| `/api/stadiums/:stadiumId/day-schedules/bulk` | `POST`   | Create or update multiple day schedules | `schedules`                 |
| `/api/day-schedules/:id`                      | `GET`    | Get day schedule by ID                  | -                           |
| `/api/day-schedules/:id`                      | `PATCH`  | Update day schedule                     | `day_of_week`, `time_slots` |
| `/api/day-schedules/:id`                      | `DELETE` | Delete day schedule                     | -                           |

## Session Templates

> [!info] Base URLs
> - Stadium templates: `/api/stadiums/:stadiumId/session-templates`
> - Individual templates: `/api/session-templates`

| Endpoint                                     | Method   | Description                             | Parameters                                                        |
| -------------------------------------------- | -------- | --------------------------------------- | ----------------------------------------------------------------- |
| `/api/stadiums/:stadiumId/session-templates` | `GET`    | Get all session templates for a stadium | -                                                                 |
| `/api/stadiums/:stadiumId/session-templates` | `POST`   | Create a session template               | `name`, `description`, `duration_minutes`, `price`, `max_players` |
| `/api/session-templates/:id`                 | `GET`    | Get session template by ID              | -                                                                 |
| `/api/session-templates/:id`                 | `PATCH`  | Update session template                 | Any template fields                                               |
| `/api/session-templates/:id`                 | `DELETE` | Delete session template                 | -                                                                 |
| `/api/session-templates/:id/toggle-status`   | `PATCH`  | Toggle active status of template        | -                                                                 |

## Available Sessions

> [!info] Base URL
> All available session endpoints use base URL: `/api/available-sessions`

| Endpoint | Method | Description | Parameters |
| -------- | ------ | ----------- | ---------- |
| `/` | `GET` | Get all available sessions | Optional: `date`, `status`, `stadium_id` |
| `/:id` | `GET` | Get available session by ID | - |
| `/` | `POST` | Create an available session | `stadium_id`, `template_id`, `date`, `start_time`, `end_time`, etc.|
| `/bulk` | `POST` | Create multiple available sessions | Array of session data |
| `/:id` | `PATCH` | Update available session | Any session fields |
| `/:id` | `DELETE` | Delete available session | - |
| `/owner` | `GET` | Get all available sessions for the current owner | Optional: `startDate`, `endDate` |

## Bookings

> [!info] Base URL
> All booking endpoints use base URL: `/api/bookings`

| Endpoint                                      | Method  | Description                        | Parameters                                        |
| --------------------------------------------- | ------- | ---------------------------------- | ------------------------------------------------- |
| `/my-bookings`                                | `GET`   | Get current user's bookings        | -                                                 |
| `/`                                           | `POST`  | Create a new booking               | `timeslot_id`, `session_id`, `player_count`, etc. |
| `/:id/status`                                 | `PATCH` | Update booking status              | `status`                                          |
| `/owner-bookings`                             | `GET`   | Get bookings for owner's stadiums  | -                                                 |
| `/:id/payment`                                | `PATCH` | Update payment status              | `payment_status`                                  |
| `/:id/assign-referee`                         | `PATCH` | Assign referee to booking          | `referee_id`, `assign_to_session`                 |
| `/:id/available-referees`                     | `GET`   | Get available referees for booking | -                                                 |
| `/api/available-sessions/:sessionId/bookings` | `GET`   | Get all bookings for a session     | -                                                 |

## Referee Management

> [!info] Base URL
> All referee endpoints use base URL: `/api/referees`

| Endpoint                   | Method   | Description                      | Parameters                                      |
| -------------------------- | -------- | -------------------------------- | ----------------------------------------------- |
| `/`                        | `GET`    | Get all referees                 | -                                               |
| `/:id`                     | `GET`    | Get referee by ID                | -                                               |
| `/user/:userId`            | `GET`    | Get referee by user ID           | -                                               |
| `/`                        | `POST`   | Create a new referee             | `name`, `email`, `phone`, `rate_per_hour`, etc. |
| `/:id`                     | `PATCH`  | Update referee                   | Any referee fields                              |
| `/:id`                     | `DELETE` | Delete referee                   | -                                               |
| `/:id/assign/:sessionId`   | `PATCH`  | Assign referee to session        | -                                               |
| `/:id/unassign/:sessionId` | `PATCH`  | Unassign referee from session    | -                                               |
| `/:id/sessions`            | `GET`    | Get sessions assigned to referee | -                                               |

## Admin Management  

> [!info] Base URL
> All admin endpoints use base URL: `/api/admin`

| Endpoint                  | Method   | Description                  | Parameters                                        |
| ------------------------- | -------- | ---------------------------- | ------------------------------------------------- |
| `/users`                  | `GET`    | List all users               | Optional: `limit`, `page`, `user_type`            |
| `/users`                  | `POST`   | Create a user                | `name`, `email`, `phone`, `password`, `user_type` |
| `/users/:id`              | `GET`    | Get user by ID               | -                                                 |
| `/users/:id`              | `PATCH`  | Update user                  | Any user fields                                   |
| `/users/:id`              | `DELETE` | Delete user                  | -                                                 |
| `/users/:id/toggle-block` | `PATCH`  | Toggle user account blocking | -                                                 |
| `/stadiums`               | `GET`    | List all stadiums            | Optional: `limit`, `page`, `status`               |
| `/bookings`               | `GET`    | List all bookings            | Various filter parameters                         |
  
## Data Models

### User

> [!note] User Model
> Core user data model for authentication and authorization

- `name`: String (required)
- `email`: String (required, unique)
- `phone`: String (required)
- `password_hash`: String (required)
- `user_type`: String (enum: 'admin', 'owner', 'player')
- `is_blocked`: Boolean (default: false)
- `created_at`: Date
- `updated_at`: Date
### Stadium

> [!note] Stadium Model
> Represents a physical stadium that can be booked

- `owner_id`: ObjectId (reference to [[#User]])
- `name`: String (required)
- `location`: String (required)
- `description`: String (required)
- `sport_type`: String (enum: 'football', 'basketball', 'tennis', 'paddle', 'volleyball', 'other')
- `capacity`: Number (required)
- `hourly_rate`: Number (required)
- `photos`: Array of Strings
- `status`: String (enum: 'active', 'inactive', 'maintenance')
- `created_at`: Date
- `updated_at`: Date
### Booking

> [!note] Booking Model
> Represents a reservation for a stadium session

- `timeslot_id`: ObjectId (required)
- `session_id`: ObjectId (reference to Available Session)
- `player_id`: ObjectId (reference to [[#User]])
- `referee_id`: ObjectId (reference to [[#Referee]], optional)
- `player_count`: Number (default: 1)
- `booking_date`: Date
- `payment_status`: String (enum: 'pending', 'paid', 'refunded', 'failed')
- `payment_amount`: Number (required)
- `status`: String (enum: 'pending', 'confirmed', 'cancelled', 'completed', 'no-show', 'rejected')
- `created_at`: Date
- `updated_at`: Date
### Referee

> [!note] Referee Model
> Represents a referee who can be assigned to sessions

- `name`: String (required)
- `email`: String (required)
- `phone`: String (required)
- `user_id`: ObjectId (reference to [[#User]], optional)
- `status`: String (enum: 'active', 'inactive')
- `rate_per_hour`: Number (required)
- `referee_type`: String (enum: 'football', 'basketball', 'tennis', 'paddle', 'volleyball', 'multi-sport', 'other')
- `description`: String
- `created_at`: Date
- `updated_at`: Date