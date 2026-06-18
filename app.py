import streamlit as st
from dataclasses import dataclass, field
from typing import List

# 1. DEFINICIÓN DE LOS REGISTROS (MODELO DE DATOS)
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

# 2. INICIALIZACIÓN DEL CATÁLOGO EN LA SESIÓN DE STREAMLIT
if "catalogo" not in st.session_state:
    st.session_state.catalogo = [
        ProductoMundial("CAM-ARG86-DIEGO", "Camiseta Argentina 1986 (Maradona)", "Réplica oficial de la mítica camiseta azul del partido contra Inglaterra.", "Camiseta", 1986, "Nuevo", 45000.0, 45000.0, 8),
        ProductoMundial("ALB-GER06-COMP", "Álbum Alemania 2006 Completo", "Álbum original de Panini con las 596 figuritas pegadas a la perfección.", "Figurita/Álbum", 2006, "Usado", 80000.0, 56000.0, 1), # 30% desc por usado
        ProductoMundial("VU-RSA10-ZUMI", "Vuvuzela Sudáfrica 2010", "Souvenir ruidoso original de color amarillo. Desatá la fiesta mundialista.", "Souvenir", 2010, "Nuevo", 6000.0, 6000.0, 15),
        ProductoMundial("FIG-QAT22-MESSI", "Figurita Lionel Messi Legend Gold", "Sticker especial extra de Panini Qatar 2022. Altamente codiciada.", "Figurita/Álbum", 2022, "Nuevo", 25000.0, 25000.0, 3),
        ProductoMundial("CAM-BRA02-RONY", "Camiseta Brasil 2002 Usada", "Camiseta original de la selección de Brasil pentacampeona. Presenta sutil desgaste.", "Camiseta", 2002, "Usado", 35000.0, 24500.0, 2), # 30% desc por usado
    ]

if "carrito" not in st.session_state:
    st.session_state.carrito = []

if "perfil" not in st.session_state:
    st.session_state.perfil = {"nombre": "", "email": "", "direccion": "", "activo": False}

# 3. INTERFAZ DE USUARIO (FRONTEND)
st.set_page_config(page_title="The Gold Cup's Mall", page_icon="🏆", layout="wide")
st.title("🏆 The Gold Cup's Mall")
st.subheader("Marketplace Exclusivo de Coleccionables de la Copa Mundial de la FIFA")

# Sidebar: Estado del Perfil / Autenticación
st.sidebar.header("👤 Mi Perfil")
if not st.session_state.perfil["activo"]:
    st.sidebar.warning("Navegando como Invitado. Debes registrarte para poder comprar.")
    with st.sidebar.form("registro_form"):
        nombre = st.text_input("Nombre Completo")
        email = st.text_input("Correo Electrónico")
        direccion = st.text_input("Dirección de Envío")
        registrar = st.form_submit_button("Crear Perfil")
        if registrar and nombre and email and direccion:
            st.session_state.perfil = {"nombre": nombre, "email": email, "direccion": direccion, "activo": True}
            st.sidebar.success(f"¡Bienvenido, {nombre}!")
            st.rerun()
else:
    st.sidebar.success(f"Conectado como: {st.session_state.perfil['nombre']}")
    st.sidebar.text(f"📍 {st.session_state.perfil['direccion']}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.perfil = {"nombre": "", "email": "", "direccion": "", "activo": False}
        st.rerun()

# Pestañas Principales de la Tienda
tab_catalogo, tab_carrito, tab_admin = st.tabs(["🛍️ Catálogo y Búsqueda", "🛒 Mi Carrito", "⚙️ Panel de Eventos (Simulación de Ofertas)"])

# --- PESTAÑA 1: CATÁLOGO, BUSCADOR Y FILTROS ---
with tab_catalogo:
    col_busq, col_filt1, col_filt2 = st.columns([2, 1, 1])
    
    with col_busq:
        busqueda = st.text_input("🔍 ¿Qué estás buscando? (Ej: 'Argentina', 'Messi', 'Vuvuzela')", "").lower()
    with col_filt1:
        cat_seleccionada = st.selectbox("Filtrar por Categoría", ["Todos", "Camiseta", "Figurita/Álbum", "Souvenir"])
    with col_filt2:
        cond_seleccionada = st.selectbox("Filtrar por Condición", ["Todos", "Nuevo", "Usado"])

    # Aplicación de Algoritmos de Filtro sobre el Registro
    productos_filtrados = []
    for prod in st.session_state.catalogo:
        coincide_busqueda = busqueda in prod.nombre.lower() or busqueda in prod.descripcion.lower()
        coincide_cat = cat_seleccionada == "Todos" or prod.categoria == cat_seleccionada
        coincide_cond = cond_seleccionada == "Todos" or prod.condicion == cond_seleccionada
        
        if coincide_busqueda and coincide_cat and coincide_cond:
            productos_filtrados.append(prod)

    # Despliegue en grilla de productos
    if productos_filtrados:
        for p in productos_filtrados:
            with st.container():
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.markdown(f"### {p.nombre} ({p.anio_mundial})")
                    st.text(f"SKU: {p.codigo_sku} | Categoría: {p.categoria} | Condición: {p.condicion}")
                    st.write(p.descripcion)
                with c2:
                    if p.condicion == "Usado":
                        st.metric("Precio Final", f"${p.precio_final:,.2f}", delta="-30% por Usado")
                    else:
                        st.metric("Precio Final", f"${p.precio_final:,.2f}")
                    st.caption(f"Stock disponible: {p.stock} unidades")
                with c3:
                    st.write("") # Espaciador
                    if p.stock > 0:
                        if st.button("Añadir al Carrito", key=p.codigo_sku):
                            st.session_state.carrito.append({"sku": p.codigo_sku, "nombre": p.nombre, "precio": p.precio_final})
                            st.toast(f"Añadido: {p.nombre}")
                    else:
                        st.error("Agotado")
                st.markdown("---")
    else:
        st.info("No se encontraron productos mundialistas que coincidan con los filtros aplicados.")

# --- PESTAÑA 2: CARRITO DE COMPRAS ---
with tab_carrito:
    st.header("Tu Carrito de Compras")
    if not st.session_state.carrito:
        st.write("El carrito está vacío. ¡Explorá el catálogo e incorporá recuerdos históricos!")
    else:
        total = 0.0
        for item in st.session_state.carrito:
            st.write(f"• **{item['nombre']}** — ${item['precio']:,.2f}")
            total += item['precio']
        
        st.markdown(f"### Total a Pagar: **${total:,.2f}**")
        
        if st.button("Confirmar y Procesar Compra 💳"):
            if not st.session_state.perfil["activo"]:
                st.error("❌ Bloqueo de Seguridad: Debes completar tu perfil en la barra lateral izquierda antes de realizar una compra.")
            else:
                st.success(f"🎉 ¡Compra procesada con éxito, {st.session_state.perfil['nombre']}! Tu pedido va en camino a {st.session_state.perfil['direccion']}.")
                st.session_state.carrito = [] # Vaciar carrito

# --- PESTAÑA 3: SIMULACIÓN DE EVENTOS EN VIVO (ACTUALIZACIÓN DINÁMICA) ---
with tab_admin:
    st.header("⚙️ Panel de Control de Eventos de la FIFA")
    st.write("Simulá eventos mundiales reales para ver cómo alteran algorítmicamente los precios del catálogo en tiempo real.")
    
    col_ev1, col_ev2 = st.columns(2)
    with col_ev1:
        if st.button("🔥 ¡Hito Histórico! Descuento del 20% en todo lo relacionado a 'Argentina'"):
            for prod in st.session_state.catalogo:
                if "argentina" in prod.nombre.lower() or "diego" in prod.nombre.lower():
                    prod.precio_final = prod.precio_final * 0.8
            st.success("Precios del catálogo actualizados para los productos de Argentina.")
            st.rerun()
            
    with col_ev2:
        if st.button("⭐ ¡Pentacampeón! Descuento del 15% en todo lo relacionado a 'Brasil'"):
            for prod in st.session_state.catalogo:
                if "brasil" in prod.nombre.lower():
                    prod.precio_final = prod.precio_final * 0.85
            st.success("Precios del catálogo actualizados para los productos de Brasil.")
            st.rerun()
