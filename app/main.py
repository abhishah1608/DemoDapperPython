from pythonnet import load
from app.Model.user import User
load("coreclr")
import clr

# Load the main DLL
dll_path = r"\python_Demo_proj\dlls\api.DapperService.dll"  # Replace with the path to your DLL
clr.AddReference(dll_path)
print("Main DLL loaded successfully.")

# Import the namespace and classes
from api.DapperService import DapperService
from Microsoft.Data.SqlClient import SqlConnection

# Initialize the SQL connection
connection_string = (
    "Server=192.168.2.141,52284;"
    "Database=OnlineCourse;"
    "User Id=abhitest;"
    "Password=Abhi123@.;"
    "Encrypt=true;"
    "TrustServerCertificate=true;"
)
sql_connection = SqlConnection(connection_string)

# Create an instance of DapperService
service = DapperService(sql_connection)
# Execute a query
count = service.ExecuteScalar("select count(*) from users", None)
print(count)