# LETS GO BELAJAR FASTAPI

from fastapi import FastAPI

# create instance
app = FastAPI()

# GET / - Root
@app.get("/")
def fn_for_rooth_get_path():
    """
    Ini adalah fungsi untuk GET / root path
    """
    
    return {
        "Halo": "Dunia"
    }
    
# GET /barang/angka_dari_user
@app.get("/barang/{angka_dari_user}")
def fn_get_list_barang_berdasarkan_angka_dari_user(angka_dari_user: int):
    print(f"Angka dari user adalah {angka_dari_user}")
    print(f"Tipe data dari angka adalah {type(angka_dari_user)}")
    return {"hello": "world"}

items = []

# GET /items
@app.get("/items")
def fn_get_list_items():
    return items 

# POST /items
@app.post("/items")
def fn_post_list_items(barangku: dict):
    print(f"Barang dari user adalah {barangku}")
    return {"messege": "Tambah items belum diimplementasikan"}
    
