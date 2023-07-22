import pickle
import connect_provider

con_obj = connect_provider.test_Provider()

connection = con_obj.connected()
print(connection)

info_block = con_obj.info()
print(info_block)

# with open("temp_files/con.pickle", "wb") as f1:
#     pickle.dump(connection, f1)
#
# with open("temp_files/inf.pickle", "wb") as f2:
#     pickle.dump(info_block, f2)

