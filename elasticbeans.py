import boto3
from iam_role import create_iam_role

eb_client = boto3.resource('elasticbeanstalk')

def create_application():
    eb_client.create_application(
        ApplicationName='DevOpsGettingStarted',
        Description='Hosting web app to test CI/CD using github'
    )
def create_environment():
    eb_client.create_environment(
        ApplicationName = "DevOpsGettingStarted",
        EnvironmentName = "DevOpsGettingStarted-env",
        Description="elastic beanstalk environment for CI delivery using github",
        SolutionStackName = '64bit Amazon Linux 2 v3.3.6 running Node.js 14',
        CNAMEPrefix='devopsgettingstarted',
        OptionSettings=[
            {
                'Namespace': 'aws:autoscaling:launchconfiguration',
            }
        ],
        Tier={
            'Name':'WebServer',
            'Type': 'Standard',
            'Version': '1.0'
        }
    )

def create_platform():
    eb_client.create_platform_version(
        PlatformName='Node.js',
        PlatformVersion="6.0.0 (Recommended)",
        EnvironmentName = "DevOpsGettingStarted-env"
    )

def main():
    create_application()
    create_application()
    create_iam_role('aws-elasticbeanstalk-ec2-role')
    create_platform()


if __name__=="__main__":
    main()