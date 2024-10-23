from models.__init__ import CONN, CURSOR

class Questions:
    
    all=[]

    def __init__(self, text, correct_answer,animal_id):
        self.id = None
        self.text = text
        self.correct_answer = correct_answer 
        self.animal_id = animal_id
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        if type(value) == str:
            self._text = value
        else:
            raise TypeError("Question must be a string")
        
    @property
    def correct_answer(self):
        return self._correct_answer
    
    @correct_answer.setter
    def correct_answer(self, value):
        if type(value) == int:
            self._correct_answer = value
        else:
            raise TypeError("Correct answer must be a integer")
    
    @property
    def animal_id(self):
        return self._animal_id
    
    @animal_id.setter
    def animal_id(self,value):
        if type(value) == int:
            self._animal_id=value
        else:
            raise TypeError("animal id must be a integer")
        
    @classmethod 
    def create_table (cls): 
        sql = """
        CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY, 
        text TEXT,
        correct_answer INTEGER,
        animal_id INTEGER)
        """ 
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table (cls):
        sql = """
            DROP TABLE IF EXISTS questions 
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        question = cls(row[1],row[2],row[3])
        question.id = row[0]
        return question
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM questions
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
            SELECT * FROM questions
        """

        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO questions(text, correct_answer, animal_id)
            VALUES (?, ?, ?)
            """
        CURSOR.execute(sql,(self.text, self.correct_answer, self.animal_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Questions.all.append(self)


    @classmethod
    def create(cls, text, correct_answer, animal_id):
        question = cls(text, correct_answer, animal_id)
        question.save()
        return question
    
    def delete(self):
        sql = """
            DELETE FROM questions
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Questions.all = [question for question in Questions.all if question.id != self.id]


    def animals(self):
        from models.animals import Animals
        sql = """
            SELECT * FROM animals
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (self.animal_id,)).fetchone()
        if row:
            return Animals.instance_from_db(row)
        else:
            return None
    
    def __repr__(self):
        return f"<Question # {self.id}: Animal Question ={self.text} Correct answer = {self.correct_answer} Animal id = {self.animal_id}>"