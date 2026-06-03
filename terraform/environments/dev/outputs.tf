output "vpc_id" {
  description = "VPC ID from networking module."
  value       = module.networking.vpc_id
}

output "public_subnet_ids" {
  description = "Public subnet IDs from networking module."
  value       = module.networking.public_subnet_ids
}

output "log_group_name" {
  description = "CloudWatch log group name for the application."
  value       = module.logging.log_group_name
}
