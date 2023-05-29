
import sqlite3

class ConfigEngine:
    
    def engine_conn(self):
        
        self.__engine_conn = 'databases.db'
        return self.__engine_conn
    
    def connection(self):
        
        try:
            self.db_name = self.engine_conn()
            
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

            return self.conn
        
        except sqlite3.Error:
            print("Erro ao inicializar o banco")
            return None
        