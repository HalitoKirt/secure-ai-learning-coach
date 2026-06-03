# Secure AI Learning Platform Architecture

## Purpose

This document describes the current architecture, security controls, trust boundaries, and planned AWS deployment architecture for the Secure AI Learning Platform.

The objective of the project is to demonstrate practical AI security engineering through secure application design, layered controls, observability, and cloud-native security patterns.

---

# Current Architecture

## Overview

The current implementation operates as a local-first architecture designed to validate AI security controls before cloud deployment.

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
Security Telemetry
```

---

# Current Components

## FastAPI Application

Acts as the primary application entry point.

Responsibilities:

* Request handling
* Authentication validation
* Security inspection
* Agent routing
* Response management

---

## Authentication Layer

Current implementation uses API key authentication.

Responsibilities:

* Verify authorized access
* Reject unauthenticated requests
* Support future migration to stronger authentication methods

---

## Rate Limiting

Protects the application from abuse and excessive requests.

Responsibilities:

* Request counting
* Abuse prevention
* Resource protection

---

## Prompt Injection Risk Detection

Inspects requests for known prompt injection indicators.

Examples:

* Ignore previous instructions
* Reveal system prompt
* Bypass security controls
* Jailbreak attempts

Actions:

* Allow
* Warn
* Block

based on policy configuration.

---

## Policy Engine

Provides centralized decision logic.

Responsibilities:

* Risk classification
* Enforcement actions
* Security policy evaluation

---

## RAG Retrieval Layer

Retrieval-Augmented Generation (RAG) provides controlled context to AI agents.

Current implementation:

* ChromaDB vector database
* SentenceTransformer embeddings
* AWS security reference content

Objectives:

* Improve response quality
* Reduce hallucinations
* Limit unauthorized knowledge access

---

## Context Guardrails

Review retrieved context before agent execution.

Responsibilities:

* Remove unsafe content
* Limit excessive context exposure
* Prevent disclosure of protected information

---

## Task-Specific AI Agents

### Tutor Agent

Educational explanations and guided learning.

### Quiz Agent

Knowledge assessment and question generation.

### Evaluator Agent

Response evaluation and scoring.

### Security Agent

Security-focused analysis and risk review.

### PQC Agent

Post-Quantum Cryptography education and risk awareness.

Focus areas:

* NIST PQC standards
* Harvest Now, Decrypt Later
* Cryptographic migration planning
* Quantum threat awareness

---

## Output Guardrails

Review responses before returning results.

Responsibilities:

* Sensitive content filtering
* Response inspection
* Output sanitization

---

## Security Telemetry

Structured JSON logging provides observability.

Collected data:

* Request IDs
* Trace IDs
* Risk levels
* Agent execution details
* Processing duration
* Security events

---

# Trust Boundaries

## Boundary 1 – User Input

Risk:

* Prompt injection
* Abuse
* Malicious requests

Controls:

* API authentication
* Rate limiting
* Prompt inspection

---

## Boundary 2 – Retrieval Layer

Risk:

* Unsafe context
* Excessive context exposure
* Data leakage

Controls:

* Context filtering
* Retrieval review
* Controlled knowledge sources

---

## Boundary 3 – Agent Execution

Risk:

* Unsafe model behavior
* Excessive responses
* Inappropriate outputs

Controls:

* Policy enforcement
* Agent-specific controls
* Output guardrails

---

# Security Architecture

Current security controls include:

| Control            | Purpose                    |
| ------------------ | -------------------------- |
| API Authentication | Access control             |
| Rate Limiting      | Abuse prevention           |
| Prompt Inspection  | Injection detection        |
| Policy Engine      | Enforcement decisions      |
| Context Guardrails | Retrieval protection       |
| Output Guardrails  | Response review            |
| Telemetry          | Detection and auditability |

---

# Target AWS Architecture

## Design Goals

* Public deployment
* Secure ingress
* Centralized observability
* Infrastructure as Code
* Security-first architecture

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
FastAPI Container
   │
   ├── CloudWatch Logs
   │
   ├── CloudWatch Metrics
   │
   ├── S3
   │
   └── Systems Manager Parameter Store
```

---

# Planned AWS Security Controls

## Edge Security

* CloudFront
* AWS WAF
* HTTPS enforcement

## Identity and Access Management

* IAM Roles
* Least Privilege
* Service-to-service permissions

## Observability

* CloudWatch Logs
* CloudWatch Metrics
* Structured telemetry

## Secrets Management

* Systems Manager Parameter Store
* KMS encryption

## Infrastructure as Code

* Terraform modules
* Version-controlled infrastructure
* Repeatable deployments

---

# Terraform Strategy

Planned modules:

```text
terraform/
├── modules/
│   ├── networking/
│   ├── security/
│   ├── compute/
│   ├── logging/
│   └── storage/
│
└── environments/
    └── dev/
```

Objectives:

* Modular design
* Reusable infrastructure
* Reduced configuration drift
* Security review through code

---

# Future Enhancements

* AWS deployment
* Terraform automation
* Enhanced telemetry
* Security dashboards
* Advanced adversarial testing
* Continuous security validation
* Expanded AI security controls

---

# Architecture Status

Current State:
Local security engineering prototype

Next Milestone:
AWS deployment using ECS Fargate and Terraform-managed infrastructure

Long-Term Goal:
Demonstrate secure AI application architecture using cloud-native security controls, observability, and infrastructure as code.
