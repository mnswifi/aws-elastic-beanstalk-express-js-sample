import boto3

eb_client = boto3.resource('elasticbeanstalk')

eb_client.create_application(
    ApplicationName='DevOpsGettingStarted',
    Description='Hosting web app to test CI/CD using github'
)

eb_client.create_environment(
    ApplicationName = "DevOpsGettingStarted",
    EnvironmentName = "DevOpsGettingStarted-env",
    Description="elastic beanstalk environment for CI delivery using github",
    Tier={
        'Name':'WebServer',
        'Type': 'Standard'
    }
)
eb_client.create_platform_version(
    PlatformName='Node.js',
    PlatformVersion="6.0.0 (Recommended)",
    EnvironmentName = "DevOpsGettingStarted-env"
)