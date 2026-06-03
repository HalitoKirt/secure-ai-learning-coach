# ADR-001: Use ECS Fargate as the AWS Deployment Target

## Status

Accepted

Date: June 2026

---

# Context

The Secure AI Learning Platform currently operates as a local security engineering prototype built with FastAPI, ChromaDB, Retrieval-Augmented Generation (RAG), task-specific AI agents, telemetry, and layered security controls.

The next major milestone is deployment to AWS.

A deployment target must be selected that supports:

* FastAPI application hosting
* Future AI platform growth
* Security-focused architecture
* Infrastructure as Code (Terraform)
* Operational observability
* Cost control
* Public demonstration capabilities

The primary options considered were:

* AWS Lambda
* Amazon ECS with AWS Fargate

---

# Decision

The project will use:

**Amazon ECS with AWS Fargate**

as the primary AWS deployment target.

---

# Options Considered

## Option 1: AWS Lambda

### Advantages

* Fully serverless
* Minimal infrastructure management
* Lower cost for very low traffic workloads
* Fast deployment for simple APIs

### Disadvantages

* Additional complexity for FastAPI adaptation
* Increased complexity for future AI workflows
* Less representative of containerized application platforms
* Less exposure to container security concepts
* Less opportunity to demonstrate container operations and orchestration

---

## Option 2: Amazon ECS with AWS Fargate

### Advantages

* Runs FastAPI natively in containers
* Supports future platform growth
* Aligns with modern application deployment patterns
* Demonstrates containerization skills
* Provides stronger Terraform learning opportunities
* Supports realistic production architecture patterns
* Enables future observability and security expansion

### Disadvantages

* Increased architectural complexity
* More AWS services involved
* Slightly higher operational overhead

---

# Rationale

The Secure AI Learning Platform is evolving into a security-focused application platform rather than a simple API.

Containerized deployment better reflects how modern AI-enabled applications are commonly operated in production environments.

Using ECS Fargate allows the project to demonstrate:

* Application security
* Cloud security
* Container security
* Infrastructure as Code
* Operational observability
* Secure deployment practices

These skills align closely with modern Cloud Security Engineer and Platform Security Engineer responsibilities.

---

# Security Considerations

The architecture will include:

* CloudFront
* AWS WAF
* HTTPS enforcement
* IAM least-privilege access
* CloudWatch logging
* Structured telemetry
* Systems Manager Parameter Store
* Security-focused Terraform modules

Public access will be protected through:

* WAF protections
* Rate limiting
* Application-level controls
* Cost monitoring
* CloudWatch alarms

---

# Cost Management Strategy

Cost exposure is a design consideration.

The platform will implement:

* AWS Budgets
* Budget alerts
* ECS service scaling limits
* Application rate limiting
* Controlled public access
* CloudWatch monitoring

These controls reduce the risk of excessive usage or abuse creating unexpected AWS costs.

---

# Consequences

Positive outcomes:

* Stronger cloud engineering portfolio
* Stronger Terraform portfolio
* Exposure to containerized workloads
* Improved operational visibility
* More realistic production architecture

Tradeoffs:

* Increased deployment complexity
* Additional AWS services to manage
* Slightly higher learning curve

The benefits are considered to outweigh the additional complexity.

---

# Future Review

This decision should be reviewed if:

* Platform requirements change significantly
* Cost considerations become prohibitive
* A future serverless architecture provides a stronger fit

Current assessment:

**ECS Fargate remains the preferred deployment target for this project.**

