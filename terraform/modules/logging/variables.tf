variable "project_name" {
  description = "Project name used for resource naming and tagging."
  type        = string
}

variable "environment" {
  description = "Deployment environment name."
  type        = string
}

variable "log_retention_days" {
  description = "Number of days to retain CloudWatch logs."
  type        = number
  default     = 14
}

