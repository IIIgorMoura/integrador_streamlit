import folium

# Coordenadas aproximadas das cidades
polo_coords = {
    'Cubatão': (-23.8956, -46.4249),
    'Mauá': (-23.6675, -46.4612),
    'Santo André': (-23.6639, -46.5386),
    'São Bernardo do Campo': (-23.6915, -46.5658),
    'Diadema': (-23.6829, -46.6197),
    'Paulínia': (-22.7472, -47.1564),
}

# Cria um mapa centrado na região do Grande ABC e Paulínia
mapa = folium.Map(location=[-23.65, -46.55], zoom_start=9)

# Adiciona marcadores para cada cidade
for cidade, coords in polo_coords.items():
    folium.Marker(location=coords, popup=cidade, tooltip=cidade).add_to(mapa)

# Salva o mapa em um arquivo HTML
mapa.save('mapa_polos_petroquimicos.html')

print("Mapa gerado e salvo como 'mapa_polos_petroquimicos.html'")