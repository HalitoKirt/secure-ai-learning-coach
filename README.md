# Secure AI Learning Platform

## Overview

Secure AI Learning Platform is an active security engineering project focused on designing, building, and securing modern AI applications.

The project combines Retrieval-Augmented Generation (RAG), task-specific AI agents, security guardrails, policy-based controls, telemetry, and threat modeling to demonstrate how AI systems can be built with security, auditability, and operational visibility from the start.

Unlike many AI demonstrations that focus exclusively on model output, this project focuses on the surrounding security architecture required to operate AI systems responsibly.

## Project Status

Current Phase: Local Security Engineering Prototype

Status:
- Core application functionality implemented
- Security controls implemented
- Telemetry and audit logging implemented
- AWS deployment architecture in design
- Terraform implementation planned

Next Major Milestone:
Deploy platform to AWS using ECS Fargate and Terraform-managed infrastructure.

---

## Project Goals

* Design secure AI application architecture
* Implement layered security controls around LLM workflows
* Reduce prompt injection and unsafe input risks
* Improve observability through structured telemetry and tracing
* Demonstrate secure RAG design patterns
* Apply cloud security engineering principles to AI systems
* Build a future AWS-hosted deployment using Infrastructure as Code (Terraform)

---

## Current Architecture

```text
Client
   │
   ▼
FastAPI Application
   │
   ▼
API Key Authentication
   │
   ▼
Rate Limiting
   │
   ▼
Prompt Injection Risk Detection
   │
   ▼
Policy Engine
   │
   ▼
RAG Retrieval
   │
   ▼
Context Guardrails
   │
   ▼
Task-Specific AI Agents
   │
   ▼
Output Guardrails
   │
   ▼
Security Telemetry & Tracing
```

---

## Security Controls

### Authentication

* API key validation
* Request authorization checks
* Protected API endpoints

### Abuse Prevention

* Request rate limiting
* Request inspection
* Policy-based enforcement actions

### Prompt Security

* Prompt injection risk detection
* Unsafe input identification
* High-risk request blocking
* Medium-risk request warning and logging

### Context Security

* Context filtering
* Retrieval review
* Controlled context exposure

### Output Security

* Output inspection
* Sensitive content filtering
* Response sanitization

### Telemetry & Auditability

* Structured JSON logging
* Trace IDs
* Request IDs
* Risk classification
* Agent execution tracking
* Request duration monitoring

---

## AI Components

### Tutor Agent

Provides guided explanations and educational responses.

### Quiz Agent

Generates assessment content from approved learning material.

### Evaluator Agent

Evaluates responses and provides feedback.

### Security Agent

Analyzes requests for prompt injection patterns, unsafe behavior, and policy violations.

### PQC Agent

Provides educational guidance on Post-Quantum Cryptography (PQC), including lattice-based, hash-based, and code-based cryptographic approaches.

The agent is designed to help users understand quantum computing risks, "harvest now, decrypt later" scenarios, migration planning, and emerging cryptographic standards intended to replace vulnerable public-key algorithms.

---

## Repository Structure

```text
secure-ai-learning-platform/
├── app/
├── data/
├── evals/
├── logs/
├── storage/
├── docs/
├── scripts/
├── tests/
├── README.md
└── requirements.txt

---

## Technology Stack

### Application Layer

* Python
* FastAPI

### AI Layer

* Ollama
* Llama 3.2
* Retrieval-Augmented Generation (RAG)

### Retrieval Layer

* ChromaDB
* Sentence Transformers
* Vector Embeddings

### Security Layer

* API Key Authentication
* Rate Limiting
* Prompt Injection Risk Detection
* Policy Enforcement
* Context Guardrails
* Output Guardrails

### Observability

* Structured Logging
* Security Telemetry
* Request Tracing
* Audit Logs

### Security Research Topics

- Post-Quantum Cryptography (PQC)
- Quantum Threat Modeling
- Cryptographic Migration Planning
- Harvest Now, Decrypt Later Risk Analysis

---

## Security Engineering Focus Areas

This project explores practical security challenges associated with AI systems, including:

* Prompt Injection
* Unsafe Retrieval
* Data Leakage
* Excessive Context Exposure
* Weak Authentication
* Abuse Prevention
* Monitoring and Detection
* AI Application Threat Modeling
* Post-Quantum Cryptography Readiness
* Cryptographic Agility

---

## Current Status 

### Implemented

* FastAPI application architecture
* Multi-agent workflow
* RAG implementation
* ChromaDB vector storage
* Prompt injection risk detection
* Policy engine
* Context filtering
* Output filtering
* Security telemetry
* Structured audit logging
* Request tracing
* Rate limiting
* API authentication

### Planned AWS Migration

* ECS Fargate deployment
* AWS WAF integration
* CloudWatch observability
* Terraform-managed infrastructure
* Secure secrets management
* Public demostration enviroment

---

## Planned AWS Architecture

```text
Internet
   │
   ▼
CloudFront
   │
   ▼
AWS WAF
   │
   ▼
Application Load Balancer
   │
   ▼
ECS Fargate
   │
   ▼
FastAPI Application
   │
   ├── CloudWatch Logs
   │
   ├── CloudWatch Metrics
   │
   ├── S3
   │
   └── Systems Manager Parameter Store
```

Future phases will migrate the platform to AWS using Terraform-managed infrastructure while maintaining security-first design principles.

---

## Infrastructure as Code Roadmap

Planned Terraform modules:

* Networking
* Security
* Compute
* Logging
* Storage
* Monitoring

Objectives:

* Repeatable deployments
* Version-controlled infrastructure
* Reduced configuration drift
* Security review through code
* Consistent cloud provisioning

---

## Documentation

Additional architecture and deployment documentation will be maintained in the `/docs` directory as the AWS migration progresses.

Planned documents include:

- Architecture Design
- Threat Modeling
- Security Controls
- Deployment Procedures
- Operational Runbooks
- Architecture Decision Records (ADRs)

---

## Why This Project Matters

Modern AI systems require more than model integration.

They require authentication, authorization, monitoring, logging, abuse prevention, policy enforcement, and secure architectural boundaries.

This project demonstrates practical engineering work focused on securing AI-enabled applications while applying cloud security principles that can scale into production environments.

---

## Author

Randall Tillman

Portfolio:
https://halitokirt.github.io/security-portfolio/

GitHub:
https://github.com/HalitoKirt
