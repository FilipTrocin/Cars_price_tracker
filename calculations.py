from database import establish_connection
from UI import user_input

connection = establish_connection()

dates = connection.distinct('FIRST_SEARCH')




