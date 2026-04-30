import tkinter as tk
from datetime import datetime

class RelojAdaptable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reloj Digital")
        self.root.geometry("750x450")
        self.root.minsize(650, 450)  # Tamaño mínimo pero permite expandir
        self.root.configure(bg='#0f172a')
        
        self.centrar_ventana()
        
        self.formato_24h = True
        self.mostrar_segundos = True
        
        # Contenedor principal
        main_container = tk.Frame(self.root, bg='#0f172a')
        main_container.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Tarjeta
        card = tk.Frame(main_container, bg='#1e293b', bd=0)
        card.pack(expand=True, fill='both')
        
        top_spacer = tk.Frame(card, bg='#1e293b', height=30)
        top_spacer.pack()
        
        # Frame para la hora (permite expandirse)
        hora_frame = tk.Frame(card, bg='#1e293b')
        hora_frame.pack(fill='x', padx=20)
        
        self.hora_label = tk.Label(
            hora_frame,
            font=('Courier New', 70, 'bold'),
            fg='#38bdf8',
            bg='#1e293b'
        )
        self.hora_label.pack()
        
        self.fecha_label = tk.Label(
            card,
            font=('Arial', 16),
            fg='#94a3b8',
            bg='#1e293b'
        )
        self.fecha_label.pack(pady=15)
        
        sep = tk.Frame(card, height=1, bg='#334155')
        sep.pack(fill='x', padx=50, pady=10)
        
        btn_container = tk.Frame(card, bg='#1e293b')
        btn_container.pack(pady=25)
        
        self.btn_formato = tk.Button(
            btn_container,
            text="24 Horas",
            font=('Arial', 11, 'bold'),
            bg='#0f172a',
            fg='#e2e8f0',
            activebackground='#334155',
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.cambiar_formato
        )
        self.btn_formato.pack(side='left', padx=10)
        
        self.btn_segundos = tk.Button(
            btn_container,
            text="Ocultar segundos",
            font=('Arial', 11, 'bold'),
            bg='#0f172a',
            fg='#e2e8f0',
            activebackground='#334155',
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.alternar_segundos
        )
        self.btn_segundos.pack(side='left', padx=10)
        
        bottom_spacer = tk.Frame(card, bg='#1e293b', height=30)
        bottom_spacer.pack()
        
        self.actualizar()
        self.root.mainloop()
    
    def centrar_ventana(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 750) // 2
        y = (self.root.winfo_screenheight() - 450) // 2
        self.root.geometry(f"750x450+{x}+{y}")
    
    def cambiar_formato(self):
        self.formato_24h = not self.formato_24h
        self.btn_formato.config(text="24 Horas" if self.formato_24h else "12 Horas")
        # Ajustar ancho de la ventana según el formato
        if not self.formato_24h and self.mostrar_segundos:
            self.root.geometry("800x450")  # Más ancho para 12h + segundos
        else:
            self.root.geometry("750x450")
        self.centrar_ventana()
    
    def alternar_segundos(self):
        self.mostrar_segundos = not self.mostrar_segundos
        self.btn_segundos.config(text="Ocultar segundos" if self.mostrar_segundos else "Mostrar segundos")
        # Ajustar ancho según configuración
        if not self.formato_24h and self.mostrar_segundos:
            self.root.geometry("800x450")
        else:
            self.root.geometry("750x450")
        self.centrar_ventana()
    
    def actualizar(self):
        ahora = datetime.now()
        
        if self.formato_24h:
            if self.mostrar_segundos:
                hora = ahora.strftime("%H:%M:%S")
            else:
                hora = ahora.strftime("%H:%M")
        else:
            if self.mostrar_segundos:
                hora_12 = ahora.strftime("%I:%M:%S").lstrip('0')
                ampm = ahora.strftime("%p")
                hora = f"{hora_12} {ampm}"
            else:
                hora_12 = ahora.strftime("%I:%M").lstrip('0')
                ampm = ahora.strftime("%p")
                hora = f"{hora_12} {ampm}"
        
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        
        fecha = f"{dias[ahora.weekday()]}, {ahora.day} de {meses[ahora.month-1]} de {ahora.year}"
        
        self.hora_label.config(text=hora)
        self.fecha_label.config(text=fecha)
        
        self.root.after(1000, self.actualizar)

if __name__ == "__main__":
    RelojAdaptable()
