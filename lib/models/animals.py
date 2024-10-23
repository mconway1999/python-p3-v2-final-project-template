from models.__init__ import CONN, CURSOR

class Animals:
    all=[]

    def __init__(self, animal_type):
        self.animal_type= animal_type 
        self.id = None 

    @property
    def animal_type(self):
        return self._animal_type
    
    @animal_type.setter
    def animal_type(self, value):
        if type(value) == str:
            self._animal_type = value
        else:
            raise TypeError("Animal type must be a string")

    @classmethod 
    def create_table (cls): 
     sql="""
        CREATE TABLE IF NOT EXISTS animals 
        (id INTEGER PRIMARY KEY, 
        animal_type TEXT)
        """ 
     CURSOR.execute(sql)
     CONN.commit()


    @classmethod 
    def drop_table (cls):
        sql= """
            DROP TABLE IF EXISTS animals
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        animal = cls(row[1])
        animal.id = row[0]
        return animal
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM animals
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM animals
        """

        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO animals (animal_type) VALUES (?)
        """

        CURSOR.execute(sql,(self.animal_type,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Animals.all.append(self)

    @classmethod
    def create(cls, animal_type):
        animal = cls(animal_type)
        animal.save()
        return animal
    
    def delete(self):
        sql = """
            DELETE FROM animals
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Animals.all = [animal for animal in Animals.all if animal.id != self.id]

    def questions(self):
        from models.questions import Questions
        sql = """
            SELECT * FROM questions
            WHERE animal_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Questions.instance_from_db(row) for row in rows]


    def __repr__(self):
        return f"<Animal # {self.id}: Animal Type = {self.animal_type}>"