phthon, fastAPi, Flask, uvicorn, pip, venv, activate
Pydantic, Injection, passlib
requrement, .toml, activate, project run, 


?? Target 


question - 
 1. Swagger kivabe open korbo ?
 /docs open korlei - peye jabo.
 http://127.0.0.1:8000/docs

 2. postman theke call kora jai.

 3. PostgreSQL ki dekha jai kon interface a  


python is programming language,
fastAPI is a modern web framework
flask is light weight web framework
uvirorn hocche server / ASGI Server ; as like php aritsan server
pip hocche - package installer ; as like composer
venv hocche - virtual environment ; as like vendor
activate hocche - ei project pip & python babohar koro.
Request Validation = Pydantic
Middleware = Injection
Hash::make() = passlib / bcrypt
Resource = Response Model
activate korlam source diye, now ekhon .venv diye pabo.
main.py run korbo - python -m uvicorn app.main:app --reload
package er talika create kora jai. pip freeze diye; ja diye notun vabe project setup & install kora jai.





EndPoint :
- /users
- /employee/create

model create korar por, alembic env te model import korte hobe then

migration run korle model er same field gulo niye model create hobe. - `alembic revision --autogenerate -m "create employees table"`

now, migration up to database - `alembic upgrade head`

request & request file - done 

now, db to insert, sei jonno route a session ta niye pass kore dite hobe



 ---

1. route create & trigger from postman
2. controller crete 
3. db setup 
4. model create
4. migration create 
5. DB Session তৈরি
6. Connect GUI using tableplus
7. Request
8. terminal a data dekhar jonno - print() as like dd() but stop hobe na
9. RequestFile 
10. Insert


Summary - 

আমাদের complete flow:

1. PostgreSQL install & database create
2. Database setup — `.env`, connection file, `main.py`
3. PostgreSQL-এর সাথে GUI — TablePlus
4. Packages install — SQLAlchemy, psycopg, Alembic, python-dotenv
5. Route / Endpoint create
6. Controller create
7. Model create
8. Migration create & run
9. Request validation / Pydantic schema create
10. DB Session route-এ connect
11. Controller থেকে DB insert

এরপরের natural steps হবে:

12. **Password hashing**
13. **Login**
14. **Authentication / JWT**


---



Here's a complete guide to run this Laravel 12 + Vue 3 + Inertia.js project. You have two options:

────────────────────────────────────────────────────────────────────────────────

🐳 Option 1: Docker (Easiest — Recommended)

│ Requirements: Docker Desktop must be running.

 ```bash                                                                                                                                                                          
   # 1. Go to the project directory                                                                                                                                               
   cd /Users/softzino/Documents/Learning/softzino/Softzino-Support-MVP-2                                                                                                          
                                                                                                                                                                                  
   # 2. Copy the environment file                                                                                                                                                 
   cp .env.example .env                                                                                                                                                           
                                                                                                                                                                                  
   # 3. Build the Docker image                                                                                                                                                    
   docker compose build                                                                                                                                                           
                                                                                                                                                                                  
   # 4. Generate the app key                                                                                                                                                      
   docker compose run --rm app php artisan key:generate                                                                                                                           
                                                                                                                                                                                  
   # 5. Start all services (app, nginx, mysql, queue worker, scheduler)                                                                                                           
   docker compose up -d                                                                                                                                                           
                                                                                                                                                                                  
   # 6. Run migrations and seed the database                                                                                                                                      
   docker compose exec app php artisan migrate --seed --force                                                                                                                     
                                                                                                                                                                                  
   # 7. (Optional) Run tests                                                                                                                                                      
   docker compose exec app php artisan test                                                                                                                                       
 ```                                                                                                                                                                              

✅ Open http://localhost:8000 in your browser.

────────────────────────────────────────────────────────────────────────────────

💻 Option 2: Native (PHP + MySQL locally)

│ Requirements: PHP 8.3+, Composer, Node 22+, MySQL 8 running locally.

 ```bash                                                                                                                                                                          
   # 1. Go to project directory                                                                                                                                                   
   cd /Users/softzino/Documents/Learning/softzino/Softzino-Support-MVP-2                                                                                                          
                                                                                                                                                                                  
   # 2. Copy the environment file                                                                                                                                                 
   cp .env.example .env                                                                                                                                                           
                                                                                                                                                                                  
   # 3. Install PHP dependencies                                                                                                                                                  
   composer install                                                                                                                                                               
                                                                                                                                                                                  
   # 4. Generate the app key                                                                                                                                                      
   php artisan key:generate                                                                                                                                                       
                                                                                                                                                                                  
   # 5. Install JS dependencies                                                                                                                                                   
   npm install                                                                                                                                                                    
                                                                                                                                                                                  
   # 6. Build frontend assets                                                                                                                                                     
   npm run build                                                                                                                                                                  
                                                                                                                                                                                  
   # 7. Update .env with your local MySQL credentials (DB_HOST=127.0.0.1, etc.)                                                                                                   
   # Then run migrations & seed                                                                                                                                                   
   php artisan migrate --seed                                                                                                                                                     
                                                                                                                                                                                  
   # 8. Start the Laravel dev server                                                                                                                                              
   php artisan serve                                                                                                                                                              
 ```                                                                                                                                                                              

Then in separate terminals, also run:

 ```bash                                                                                                                                                                          
   npm run dev           # Vite hot-reload (frontend)                                                                                                                             
   php artisan queue:work    # Process queued email notifications                                                                                                                 
   php artisan schedule:work # Run scheduled tasks                                                                                                                                
 ```                                                                                                                                                                              

✅ Open http://localhost:8000

────────────────────────────────────────────────────────────────────────────────

🔑 Seeded Login Accounts

┌───────────────┬────────────────────┬──────────────┐                                                                                                                            
│ Role          │ Email              │ Password     │                                                                                                                            
├───────────────┼────────────────────┼──────────────┤                                                                                                                            
│ Administrator │ admin@softzino.com │ ChangeMe123! │                                                                                                                            
├───────────────┼────────────────────┼──────────────┤                                                                                                                            
│ Agent         │ agent@softzino.com │ ChangeMe123! │                                                                                                                            
└───────────────┴────────────────────┴──────────────┘

────────────────────────────────────────────────────────────────────────────────

⚠️ Important Notes for Native Setup

Since your .env.example has DB_HOST=mysql (Docker hostname), you must change it for local:

 ```env                                                                                                                                                                           
   DB_HOST=127.0.0.1                                                                                                                                                              
   DB_USERNAME=root        # your local MySQL user                                                                                                                                
   DB_PASSWORD=your_pass   # your local MySQL password                                                                                                                            
 ```                                                                                                                                                                              

Also create the database first:

 ```sql                                                                                                                                                                           
   CREATE DATABASE softzino_support;                                                                                                                                              
 ```                                                                                                                                                                              

────────────────────────────────────────────────────────────────────────────────

My recommendation: Use Docker since the project is already Docker-configured and all services (MySQL, queue worker, scheduler, Nginx) start automatically with one command.

───────────────────────────────────────



