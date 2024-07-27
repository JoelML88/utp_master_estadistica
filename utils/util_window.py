def centrar_ventana(ventana, window_w,window_h):
    window_width= ventana.winfo_screenwidth()
    window_height= ventana.winfo_screenheight()
    x = int((window_width/2) - (window_w/2))
    y = int((window_height/2) - (window_h/2))
    return ventana.geometry(f"{window_w}x{window_h}+{x}+{y}")