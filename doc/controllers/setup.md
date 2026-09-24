# Controller

big project na hole controller dorkar hoi na, tobu o laravel er moto controller folder create kore korte paro.

```python
@router.post("/reg")
def store():
    return register()
```

- Route::get('/users', [AuthController::class, 'register']);

ekhane 2 part ache,  store ()  ja AuthController class er sathe tulona kora hoi, 

aar register() hocche - method ja controller theke asbe 