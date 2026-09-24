# Routes

- route create korar jonno akta `routes` folder create korbo. then
- akta file create korbo, laravel a jemon age theke web.php / api.php or nijera create korle seta bootstrap app a register kortam 
- ekhane module / feature wise route korte suggest kore, like - user.py, product.py, employe.py etc 
- aar swagger e jeno help hoi, segregation er jonno prefix use kora valo. like - prefix="/api"


```python
@router.get("/users")
def get_users(): ---------> eita jekono name hote pare, but convenience hoi. like eita diye buja jai ami users get kortechi
    return {
        "message": "successfully message from test api"
    }
```