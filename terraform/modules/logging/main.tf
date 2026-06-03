resource "aws_cloudwatch_log_group" "app" {
  name              = "/aws/ecs/${var.project_name}-${var.environment}"
  retention_in_days = var.log_retention_days

  tags = {
    Name        = "${var.project_name}-${var.environment}-app-logs"
    Environment = var.environment
    Project     = var.project_name
  }
}
