## Getting Started

### Prerequisites

Make sure you have Python and pip installed on your system.

# Install dependencies
pip install -r requirements.txt

# Run the application from FAST-API-TEST directory
python3 -m uvicorn main:app --reload --port 8080

#  Testing Endpoint
Go on Open Api Docs after running application: http://127.0.0.1:8080/docs
Click Drop Down on Get /vehicles
Click Try it out
Input sample model_year to test
Click Execute to run endpoint