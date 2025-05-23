import flet as ft

def main(page: ft.Page):
    page.title = "Calc App 2.1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    result = ft.Text(value="0")

    txt_end_ip = ft.TextField(label="Digite o endereço IP", hint_text="xxx.xxx.xxx.xxx", width=300)
    txt_mask = ft.TextField(label="Digite a máscara", hint_text="xxx.xxx.xxx.xxx", width=300)

    

    def btn_click(e):
        if not txt_end_ip.value:
            txt_end_ip.error_text = "Endereço IP deve estar na faixa 1.0.0.0 - 255.255.255.255"
            page.update()
        elif not txt_mask.value:
            txt_mask.error_text = "Máscara deve estar na faixa 255.0.0.0 - 255.255.255.255"
            page.update()
        else:
            name_end_ip = txt_end_ip.value
            name_mask = txt_mask.value
            page.clean()
            page.add(
                ft.Column(
                    [
                        ft.Text(f"Endereço digitado: {name_end_ip}!"),
                        ft.Text(f"Máscara digitada: {name_mask}!"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

    
    tokens = txt_end_ip.value.split(".")
    print(tokens)
    
    
    layout = ft.Column(
        controls=[
            ft.Text("Calculadora IPV4", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            txt_end_ip,
            txt_mask,
            ft.ElevatedButton("Calcular", on_click=btn_click),
            ft.Container(
                width=350,
                bgcolor=ft.Colors.BLACK,
                border_radius=ft.border_radius.all(20),
                padding=20,
                content=ft.Column(
                    controls=[ft.ElevatedButton(text="CALCULAR")]
                )
            ),
            ft.Row(controls=[result]),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="AC"),
                    ft.ElevatedButton(text="+/-"),
                    ft.ElevatedButton(text="%"),
                    ft.ElevatedButton(text="/"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="7"),
                    ft.ElevatedButton(text="8"),
                    ft.ElevatedButton(text="9"),
                    ft.ElevatedButton(text="*"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="4"),
                    ft.ElevatedButton(text="5"),
                    ft.ElevatedButton(text="6"),
                    ft.ElevatedButton(text="-"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="1"),
                    ft.ElevatedButton(text="2"),
                    ft.ElevatedButton(text="3"),
                    ft.ElevatedButton(text="+"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="0"),
                    ft.ElevatedButton(text="."),
                    ft.ElevatedButton(text="="),
                ]
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(layout)

ft.app(target=main)
