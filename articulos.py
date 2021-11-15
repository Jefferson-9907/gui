import pyodbc

class Articulos:

    def abrir(self):
        conexion=pyodbc.connect(driver='{SQL Server Native Client 11.0};', server='SERVIDOR',
                                         database='COMDELFINA', trusted_connection='yes')
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Nombre from INV_PRODUCTOS where CódigoBarra1=?"
        cursor.execute(sql, datos)
        return cursor.fetchall()
        """cone.close()"""

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE INV_PD_BODEGA_STOCK SET Stock =Stock+? FROM INV_PD_BODEGA_STOCK JOIN INV_PRODUCTOS ON INV_PD_BODEGA_STOCK.ProductoID=INV_PRODUCTOS.ID WHERE CódigoBarra1=?"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas