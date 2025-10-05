variable "AWS_ACCESS_KEY_ID" {
  description = "AWS Access Key ID"
  type        = string
  sensitive   = true
}

variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS Secret Access Key"
  type        = string
  sensitive   = true
}

variable "aws_secretsmanager_arn" {
  type        = string
  default     = "arn:aws:secretsmanager:us-east-1:135808921133:secret:prod/aws/credentials-1czvrt"
  description = "Arn of the AWS Secrets Manager secret for credentials"
}

variable "app_runner_connection_arn" {
  type        = string
  default     = "arn:aws:apprunner:us-east-1:135808921133:connection/new-connection/45c0ab0285b64f8abd68e04dde58f1ff"
  description = "ARN of the App Runner connection for GitHub"
}

variable "private_subnet_ids" {
  description = "List of private subnet IDs for secure resources (RDS, AppRunner)"
  type        = list(string)
  default     = ["subnet-0da5a520e65e987ea", "subnet-085e7a26f21079a2e", "subnet-02ae8822f384a7697", "subnet-053716f4ebdb38ece", "subnet-0fa8ce2ba22b06e57"]  # Replace with your private subnets
}

variable "aws_security_group_id" {
  type        = string
  default     = "vpc-0297cd44f118eae2f"
  description = "AWS Security Group ID for the RDS database"
}

variable "vpc_id" {
  type = string
  default = "vpc-0297cd44f118eae2f"
}

variable "ec2_security_group_id" {
  type        = string
  default     = "sg-002621f46d582b78d"
  description = "Ec2 security group ID for accessing RDS database"
}

variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region"
}

variable "customer_name" {
  type        = string
  description = "Name of the customer"
}

variable "project" {
  type        = string
  description = "Name of the project"
}

variable "repository_url" {
  type        = string
  description = "GitHub repository URL for the backend service"
}

variable "branch" {
  type        = string
  description = "Name of the repo branch"
  default     = "master"
}

variable "db_password" {
  description = "Password for the database admin user"
  type        = string
  sensitive   = true
}
variable "db_username" {
  description = "Username for the database"
  type        = string
}

variable "db_name" {
  description = "Database name"
  type        = string
}