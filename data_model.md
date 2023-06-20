# Data Model for Portfolio Maker

## User:
   - id (primary key)
   - username
   - email
   - password (hashed)
   - created_at
   - updated_at

## Domain:
   - id (primary key)
   - user_id (foreign key referencing the User table)
   - portfolio_id (foreign key referencing the Portfolio table)
   - domain_name (unique)
   - created_at

## Portfolio:
   - id (primary key)
   - user_id (foreign key referencing the User table)
   - name
   - bio
   - contact_details
   - created_at
   - updated_at

## Project:
   - id (primary key)
   - project_owner_id (foreign key referencing the User table)
   - title
   - description
   - created_at
   - updated_at

## Images:
   - id (primary key)
   - project_id (foreign key referencing the project table)
   - url (URL field to store link of s3 object)
   - decription (text field)

## Skill:
   - id (primary key)
   - name
   - created_at
   - updated_at

## ProjectSkill
   - id (primary key)
   - project_id (foreign key referencing the project table)
   - skill_id (foreign key referencing the skill table)

## PortfolioSkill (many-to-many relationship between Portfolio and Skill):
   - id (primary key)
   - portfolio_id (foreign key referencing the Portfolio table)
   - skill_id (foreign key referencing the Skill table)
