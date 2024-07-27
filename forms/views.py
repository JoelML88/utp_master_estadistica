import tkinter as tk
from tkinter import font, ttk
import utils.util_window as u_window
import utils.util_images as u_image

from PIL import Image, ImageTk

from forms.calculators import calcular_bayes, calcular_binomial, calcular_exponencial,calcular_poisson, calcular_poisson_range, calcular_normal

from forms.plotting import plot_bayes, plot_binomial, plot_exponencial, plot_poisson, plot_poisson_range, plot_normal

from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR, COLOR_BOTON_LATERAL, COLOR_BOTON_PRINCIPAL

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = u_image.read_image("./images/logo.png", (560, 136))
        self.perfil = u_image.read_image("./images/utp_color.png", (100, 100))
        self.config_window()
        self.panels()
        self.controles_barra_superior()
        self.controles_menulateral()
        self.controles_body()

    def config_window(self):
        self.title("Python GUI")
        self.iconbitmap("./images/icon.ico")
        w, h = 1024, 600
        self.geometry(f"{w}x{h}+0+0")
        u_window.centrar_ventana(self, w, h)

    def panels(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=165)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Estadística")
        self.labelTitulo.config(fg='#fff', font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.menu_hamburguesa = u_image.read_image("./images/menu.png", (20, 20))
        self.btn_lateral = tk.Button(self.barra_superior, font=font_awesome, image=self.menu_hamburguesa,
                                     command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.btn_lateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior, text="Joel Méndez León ")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

        self.labelTitulo = tk.Label(self.barra_superior, text=" Rosalba Bolaños Ortega")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menulateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.btn_dash_board = tk.Button(self.menu_lateral)
        self.btn_profile = tk.Button(self.menu_lateral)
        self.btn_picture = tk.Button(self.menu_lateral)
        self.btn_info = tk.Button(self.menu_lateral)
        self.btn_settings = tk.Button(self.menu_lateral)

        # Primero, carga la imagen que deseas usar para el botón
        self.bayes_img = u_image.read_image("./images/bayes_icon_w.png", (20, 20))

        # Crea el botón con la imagen y el texto
        btn_bayes = tk.Button(self.menu_lateral, text="Bayes", image=self.bayes_img, compound=tk.LEFT, command=self.mostrar_bayes, font=font_awesome, bd=0,
                      bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_bayes.pack(pady=5)
        #Agregamos eventos de hover
        self.bind_hover_events(btn_bayes,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)
        

        self.binomial_img = u_image.read_image("./images/bin_icon_w.png", (20, 20))
        btn_binomial = tk.Button(self.menu_lateral, text="Binomial", image=self.binomial_img, compound=tk.LEFT, command=self.mostrar_binomial, font=font_awesome, bd=0,
                      bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_binomial.pack(pady=5)
        self.bind_hover_events(btn_binomial,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)


        self.exponencial_img = u_image.read_image("./images/expo_icon_w.png", (20, 20))
        btn_exponencial = tk.Button(self.menu_lateral, text="Exponencial", image=self.exponencial_img, compound=tk.LEFT, command=self.mostrar_exponencial, font=font_awesome, bd=0,
                      bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_exponencial.pack(pady=5)
        self.bind_hover_events(btn_exponencial,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)

        self.poisson_img = u_image.read_image("./images/poison_icon_w.png", (20, 20))
        btn_poisson = tk.Button(self.menu_lateral, text="Poisson", image=self.poisson_img, compound=tk.LEFT, command=self.mostrar_poisson, font=font_awesome, bd=0,
                      bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_poisson.pack(pady=5)
        self.bind_hover_events(btn_poisson,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)

        

        self.poisson_range_img = u_image.read_image("./images/poison_range_icon_w.png", (20, 20))
        btn_poisson_range = tk.Button(self.menu_lateral, text="Poisson Range", image=self.poisson_range_img, compound=tk.LEFT, command=self.mostrar_poisson_range, 
                                      font=font_awesome, bd=0, bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_poisson_range.pack(pady=5)
        self.bind_hover_events(btn_poisson_range,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)

        

        self.normal_img = u_image.read_image("./images/normal_icon_w.png", (20, 20))
        btn_normal = tk.Button(self.menu_lateral, text="Normal", image=self.normal_img, compound=tk.LEFT, command=self.mostrar_normal, font=font_awesome, bd=0,
                      bg=COLOR_BOTON_LATERAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_normal.pack(pady=5)
        self.bind_hover_events(btn_normal,COLOR_MENU_CURSOR,COLOR_BOTON_LATERAL)
    

    def controles_body(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def bind_hover_events(self, button, bg_cursor_in, bg_cursor_out):
        button.bind("<Enter>", lambda event: self.on_enter(event, button,bg_cursor_in))
        button.bind("<Leave>", lambda event: self.on_leave(event, button,bg_cursor_out))

    def on_enter(self, event, button,color):
        button.config(bg=color, fg='white')

    def on_leave(self, event, button,color):
        button.config(bg=color, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def mostrar_bayes(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora de Bayes", [("P(A)", 'p_a_entry'), ("P(B)", 'p_b_entry'), ("P(B|A)", 'p_b_dado_a_entry')], calcular_bayes, plot_bayes)

    def mostrar_binomial(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora Binomial", [("Número de ensayos (n)", 'n_entry'), ("Número de éxitos (k)", 'k_entry'), ("Probabilidad de éxito (p)", 'p_entry')], calcular_binomial, plot_binomial)

    def mostrar_exponencial(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora Exponencial", [("Tasa de eventos (λ)", 'lam_entry'), ("Valor de x", 'x_entry')], calcular_exponencial, plot_exponencial)

    def mostrar_poisson(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora Poisson", [("Número promedio de eventos (λ)", 'lmbda_entry'), ("Número de eventos (k)", 'k_entry')], calcular_poisson, plot_poisson)

    def mostrar_poisson_range(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora Poisson Range", [("Número promedio de eventos (λ)", 'lmbda_entry'), ("Valor de k1 (inferior)", 'k1_entry'), ("Valor de k2 (superior)", 'k2_entry')], calcular_poisson_range, plot_poisson_range)

    def mostrar_normal(self):
        limpiar_frame(self.cuerpo_principal)
        self._crear_calculadora("Calculadora Normal", [("Media (μ)", 'mu_entry'), ("Desviación estándar (σ)", 'sigma_entry'), ("Valor de x", 'x_entry')], calcular_normal, plot_normal)

    def _crear_calculadora(self, titulo, entradas, funcion_calcular, funcion_graficar):
        tk.Label(self.cuerpo_principal, text=titulo, font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL).pack(pady=10)
        for texto, variable in entradas:
            tk.Label(self.cuerpo_principal, text=texto, font=("Roboto", 12), bg=COLOR_CUERPO_PRINCIPAL).pack()
            setattr(self, variable, tk.Entry(self.cuerpo_principal))
            getattr(self, variable).pack()

        self.resultado_text = tk.Text(self.cuerpo_principal, height=10, width=50, font=("Roboto", 14))
        self.resultado_text.pack(pady=10)

        font_awesome = font.Font(family='FontAwesome', size=11)

        button_frame = tk.Frame(self.cuerpo_principal)
        button_frame.pack(pady=10)

        # Primero, carga la imagen que deseas usar para el botón
        self.calcular_img = u_image.read_image("./images/calc_icon_w.png", (40, 40))
        # Crea el botón con la imagen y el texto
        btn_calcular=tk.Button(button_frame, text="Calcular Proba.", image=self.calcular_img, compound=tk.LEFT, command=lambda: funcion_calcular(self),
                               font=font_awesome,bd=0, bg=COLOR_BOTON_PRINCIPAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_calcular.pack(side=tk.LEFT, padx=5)
        self.bind_hover_events(btn_calcular,COLOR_BOTON_LATERAL, COLOR_MENU_CURSOR)


        self.grafica_img = u_image.read_image("./images/graphic_icon_w.png", (40, 40))        
        btn_mostrar_grafica = tk.Button(button_frame, text="Mostrar Gráfica", image=self.grafica_img, compound=tk.LEFT, command=lambda: funcion_graficar(self),
                                        font=font_awesome, bd=0, bg=COLOR_BOTON_PRINCIPAL, fg="white", width=165, height=40, anchor="w", padx=5)
        btn_mostrar_grafica.pack(side=tk.LEFT, padx=5)
        self.bind_hover_events(btn_mostrar_grafica,COLOR_BOTON_LATERAL, COLOR_MENU_CURSOR)


def limpiar_frame(cuerpo_principal):
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()
