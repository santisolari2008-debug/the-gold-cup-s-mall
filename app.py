import streamlit as st
from dataclasses import dataclass
from typing import List

# 1. DEFINICIÓN DEL REGISTRO PRINCIPAL (MODELO DE DATOS)
@dataclass
class ProductoMundial:
    codigo_sku: str
    nombre: str
    descripcion: str
    categoria: str
    anio_mundial: int
    condicion: str
    precio_base: float
    precio_final: float
    stock: int
    icono_visual: str

# 2. INICIALIZACIÓN DEL CATÁLOGO DE 15 PRODUCTOS EN LA SESIÓN
if "catalogo" not in st.session_state:
    st.session_state.catalogo = [
        # --- CATEGORÍA: CAMISETAS (5 productos) ---
        ProductoMundial(
            "CAM-ARG86-DIEGO", "Camiseta Argentina 1986 (Maradona)", 
            "Réplica oficial de la mítica indumentaria alternativa azul utilizada en los Cuartos de Final en México 1986.", 
            "Camiseta", 1986, "Nuevo", 45000.0, 45000.0, 8, "👕"
        ),
        ProductoMundial(
            "CAM-BRA02-RONY", "Camiseta Brasil 2002 (Ronaldo)", 
            "Prenda original de la selección brasileña pentacampeona de Corea-Japón 2002. Presenta sutiles marcas de época.", 
            "Camiseta", 2002, "Usado", 35000.0, 24500.0, 2, "👕"
        ),
        ProductoMundial(
            "CAM-ITA90-VINT", "Camiseta Italia 1990 Local", 
            "Indumentaria de la selección italiana para el mundial de Italia 90. Un clásico textil de colección premium.", 
            "Camiseta", 1990, "Nuevo", 52000.0, 52000.0, 4, "👕"
        ),
        ProductoMundial(
            "CAM-FRA98-ZIZOU", "Camiseta Francia 1998 (Zidane)", 
            "Modelo titular utilizado por la selección campeona del mundo en su torneo local. Edición histórica conmemorativa.", 
            "Camiseta", 1998, "Nuevo", 48000.0, 48000.0, 5, "👕"
        ),
        ProductoMundial(
            "CAM-GER14-FINAL", "Camiseta Alemania 2014 Visitante", 
            "Modelo alternativo negro y rojo utilizado en la campaña del campeonato de Brasil 2014. Conservada en vitrina.", 
            "Camiseta", 2014, "Usado", 38000.0, 26600.0, 1, "👕"
        ),

        # --- CATEGORÍA: FIGURITAS / ÁLBUMES (5 productos) ---
        ProductoMundial(
            "ALB-GER06-COMP", "Album Alemania 2006 Completo", 
            "Álbum oficial Panini de la Copa del Mundo Alemania 2006. Incluye las 596 figuritas pegadas de forma milimétrica.", 
            "Figurita/Álbum", 2006, "Usado", 80000.0, 56000.0, 1, "📖"
        ),
        ProductoMundial(
            "FIG-QAT22-MESSI", "Figurita Lionel Messi Legend Gold", 
            "Sticker especial Extra Gold de Panini correspondiente al Mundial de Qatar 2022. Altamente codiciada en el mercado.", 
            "Figurita/Álbum", 2022, "Nuevo", 25000.0, 25000.0, 3, "🃏"
        ),
        ProductoMundial(
            "ALB-MEX86-RETRO", "Album Mexico 1986 Panini Reimpresion", 
            "Reproducción certificada de alta fidelidad del álbum de figuritas de México 1986. Ideal para coleccionistas de la era dorada.", 
            "Figurita/Álbum", 1986, "Nuevo", 18000.0, 18000.0, 12, "📖"
        ),
        ProductoMundial(
            "FIG-BRA14-NEY", "Figurita Neymar Jr Shiny Edition", 
            "Sticker cromado brillante de edición limitada correspondiente al mundial de Brasil 2014. Excelente estado de preservación.", 
            "Figurita/Álbum", 2014, "Nuevo", 4500.0, 4500.0, 15, "🃏"
        ),
        ProductoMundial(
            "ALB-ITA90-INCOM", "Album Italia 1990 Parcial", 
            "Álbum original con el 75% de sus figuritas adheridas. Incluye secciones completas de las potencias europeas.", 
            "Figurita/Álbum", 1990, "Usado", 30000.0, 21000.0, 2, "📖"
        ),

        # --- CATEGORÍA: SOUVENIRS (5 productos) ---
        ProductoMundial(
            "VU-RSA10-ZUMI", "Vuvuzela Sudafrica 2010 Oficial", 
            "Instrumento de viento tradicional y souvenir ruidoso original en color amarillo emblemático de la Copa del Mundo.", 
            "Souvenir", 2010, "Nuevo", 6000.0, 6000.0, 20, "🎺"
        ),
        ProductoMundial(
            "BUF-FRA98-CHAMP", "Bufanda Francia 1998 Final", 
            "Bufanda conmemorativa tejida oficial del partido final entre Francia y Brasil celebrado en Saint-Denis.", 
            "Souvenir", 1998, "Usado", 12000.0, 8400.0, 3, "🧣"
        ),
        ProductoMundial(
            "PEL-QAT22-RIHLA", "Pelota Al Rihla Official Match Ball", 
            "Balón oficial de juego de la Copa Mundial de la FIFA Qatar 2022 en su empaque institucional sellado de fábrica.", 
            "Souvenir", 2022, "Nuevo", 65000.0, 65000.0, 6, "⚽"
        ),
        ProductoMundial(
            "TICK-ARG78-FINAL", "Entrada Original Final Argentina 1978", 
            "Ticket físico original del partido final disputado en el Estadio Monumental entre Argentina y Países Bajos. Pieza histórica.", 
            "Souvenir", 1978, "Usado", 95000.0, 66500.0, 1, "🎟️"
        ),
        ProductoMundial(
            "MED-USA94-REPLI", "Replica Medalla de Campeon USA 1994", 
            "Reproducción oficial a escala real con cinta institucional de la medalla otorgada a los campeones del mundo en 1994.", 
            "Souvenir", 1994, "Nuevo", 15000.0, 15000.0, 10, "🥇"
        )
    ]

if "carrito" not in st.session_state:
    st.session_state.carrito = []

if "perfil" not in st.session_state:
    st.session_state.perfil = {"nombre": "", "email": "", "direccion": "", "activo": False}

# 3. INTERFAZ DE USUARIO Y CONFIGURACIÓN VISUAL (ESTILO CORPORATIVO)
st.set_page_config(page_title="The Gold Cup's Mall", page_icon="🏆", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: bold; color: #0C2340; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size:18px !important; color: #8A7322; text-align: center; margin-bottom: 30px; font-weight: 500; }
    .product-card { background-color: #F8F9FA; border-left: 5px solid #8A7322; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
    .icon-container { font-size: 48px; text-align: center; line-height: 80px; background-color: #E9ECEF; border-radius: 8px; width: 80px; height: 80px; }
    .demo-notice { background-color: #FFF3CD; border: 1px solid #FFEBAA; color: #856404; padding: 20px; border-radius: 8px; text-align: center; margin-top: 35px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">The Gold Cup\'s Mall</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Marketplace Corporativo de Coleccionables de la Copa Mundial de la FIFA</p>', unsafe_allow_html=True)

# Sidebar: Perfil de Usuario
st.sidebar.header("Mi Perfil")
if not st.session_state.perfil["activo"]:
    st.sidebar.warning("Navegando como Invitado. Requiere autenticación para confirmar compras.")
    with st.sidebar.form("registro_form"):
        nombre = st.text_input("Nombre Completo")
        email = st.text_input("Correo Electrónico")
        direccion = st.text_input("Dirección de Envío")
        registrar = st.form_submit_button("Crear Perfil Corporativo")
        if registrar and nombre and email and direccion:
            st.session_state.perfil = {"nombre": nombre, "email": email, "direccion": direccion, "activo": True}
            st.sidebar.success(f"Sesión iniciada: {nombre}")
            st.rerun()
else:
    st.sidebar.success(f"Usuario autenticado: {st.session_state.perfil['nombre']}")
    st.sidebar.text(f"Dirección: {st.session_state.perfil['direccion']}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.perfil = {"nombre": "", "email": "", "direccion": "", "activo": False}
        st.rerun()

# Pestañas del Sistema
tab_catalogo, tab_carrito, tab_admin = st.tabs(["Catálogo de Productos", "Carrito de Compras", "Actualización Dinámica de Precios"])

# --- PESTAÑA 1: CATÁLOGO, BUSCADOR Y FILTROS ---
with tab_catalogo:
    col_busq, col_filt1, col_filt2 = st.columns([2, 1, 1])
    
    with col_busq:
        busqueda = st.text_input("Filtrar por texto (Ej: Argentina, Maradona, Pelota)", "").lower()
    with col_filt1:
        cat_seleccionada = st.selectbox("Clasificar por Categoría", ["Todos", "Camiseta", "Figurita/Álbum", "Souvenir"])
    with col_filt2:
        cond_seleccionada = st.selectbox("Clasificar por Condición", ["Todos", "Nuevo", "Usado"])

    # Procesamiento algorítmico de filtros
    productos_filtrados = []
    for prod in st.session_state.catalogo:
        coincide_busqueda = busqueda in prod.nombre.lower() or busqueda in prod.descripcion.lower() or str(prod.anio_mundial) in busqueda
        coincide_cat = cat_seleccionada == "Todos" or prod.categoria == cat_seleccionada
        coincide_cond = cond_seleccionada == "Todos" or prod.condicion == cond_seleccionada
        
        if coincide_busqueda and coincide_cat and coincide_cond:
            productos_filtrados.append(prod)

    # Renderizado
    if productos_filtrados:
        for p in productos_filtrados:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            c_icon, c_desc, c_precio, c_accion = st.columns([1, 4, 2, 1])
            
            with c_icon:
                st.markdown(f'<div class="icon-container">{p.icono_visual}</div>', unsafe_allow_html=True)
            with c_desc:
                st.markdown(f"#### {p.nombre} ({p.anio_mundial})")
                st.caption(f"Código SKU: {p.codigo_sku}  |  Categoría: {p.categoria}  |  Estado: {p.condicion}")
                st.write(p.descripcion)
            with c_precio:
                if p.condicion == "Usado":
                    st.metric("Precio de Venta", f"${p.precio_final:,.2f}", delta="Depreciado por uso")
                else:
                    st.metric("Precio de Venta", f"${p.precio_final:,.2f}")
                st.caption(f"Disponibilidad: {p.stock} unidades")
            with c_accion:
                st.write("") 
                if p.stock > 0:
                    if st.button("Añadir", key=p.codigo_sku):
                        st.session_state.carrito.append({"sku": p.codigo_sku, "nombre": p.nombre, "precio": p.precio_final})
                        st.toast(f"Producto incorporado: {p.nombre}")
                else:
                    st.error("Sin Stock")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No se registran artículos de colección mundialistas que cumplan con los criterios seleccionados.")

    # MENSAJE INFORMATIVO DE VERSIÓN DEMO (Al final del catálogo)
    st.markdown("""
        <div class="demo-notice">
            📌 <strong>Aviso del Sistema:</strong> Esta aplicación web corresponde a una versión preliminar de desarrollo (Entorno Demo). 
            El catálogo actual está limitado a 15 artículos históricos con fines de evaluación técnica de estructuras de registros y algoritmos de filtrado. 
            Próximamente se habilitará el módulo de carga masiva de inventario para la incorporación de nuevos productos y la pasarela de pagos real.
        </div>
    """, unsafe_allow_html=True)

# --- PESTAÑA 2: CARRITO DE COMPRAS ---
with tab_carrito:
    st.header("Resumen del Pedido")
    if not st.session_state.carrito:
        st.write("El carrito de compras se encuentra vacío actualmente.")
    else:
        total = 0.0
        for item in st.session_state.carrito:
            st.write(f"• **{item['nombre']}** — ${item['precio']:,.2f}")
            total += item['precio']
        
        st.markdown(f"### Importe Consolidado Total: **${total:,.2f}**")
        
        if st.button("Procesar Transacción"):
            if not st.session_state.perfil["activo"]:
                st.error("Restricción de Acceso: El sistema requiere la validación de un perfil de usuario en el panel izquierdo para concretar transacciones.")
            else:
                st.success(f"Confirmación: Compra procesada correctamente para el usuario {st.session_state.perfil['nombre']}. Remisión asignada a la dirección {st.session_state.perfil['direccion']}.")
                st.session_state.carrito = []

# --- PESTAÑA 3: ACTUALIZACIONES DE CATÁLOGO ---
with tab_admin:
    st.header("Panel de Administración y Eventos FIFA")
    st.write("Interfaz para la actualización dinámica de registros económicos del inventario basada en eventos futbolísticos en vivo.")
    
    col_ev1, col_ev2 = st.columns(2)
    with col_ev1:
        if st.button("Aplicar Bonificación Histórica: 20% de descuento para ítems asociados a Argentina"):
            for prod in st.session_state.catalogo:
                if "argentina" in prod.nombre.lower() or "diego" in prod.nombre.lower() or "messi" in prod.nombre.lower():
                    prod.precio_final = prod.precio_final * 0.8
            st.success("Registros de precios modificados exitosamente en la base de datos.")
            st.rerun()
            
    with col_ev2:
        if st.button("Aplicar Bonificación de Campeón: 15% de descuento para ítems asociados a Brasil"):
            for prod in st.session_state.catalogo:
                if "brasil" in prod.nombre.lower() or "ney" in prod.nombre.lower():
                    prod.precio_final = prod.precio_final * 0.85
            st.success("Registros de precios modificados exitosamente en la base de datos.")
            st.rerun()
