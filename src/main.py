import flet as ft


def main(page: ft.Page):

    def row_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                width=50,
                                height=50,
                            ),
                            ft.Icon(
                                ft.Icons.PETS,
                                size=30,
                                color=ft.Colors.BROWN_700
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SETTINGS,
                                icon_color=ft.Colors.BROWN_300,
                                icon_size=30
                            )
                        ],
                        alignment=align,
                        width=360,   # 추가
                    ),
                    bgcolor=ft.Colors.AMBER_100,
                    width=360,      # 추가
                ),
            ],
        )

    def nav():
        pagelet = ft.Pagelet(
            navigation_bar=ft.CupertinoNavigationBar(
                bgcolor=ft.Colors.AMBER_100,
                inactive_color=ft.Colors.BROWN_200,
                active_color=ft.Colors.BROWN_700,

                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                    ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.SHOP,
                        selected_icon=ft.Icons.SHOPPING_CART,
                        label="Shop",
                    ),
                    ft.NavigationBarDestination(icon=ft.Icons.STAR, label="AI"),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.DOOR_FRONT_DOOR,
                        selected_icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                        label="MyPage"
                    ),
                ],
            ),
            content=ft.Container(),
            height=150,
            width=360,
        )
        return pagelet

    page.add(

        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
            controls=[
                # 상단
                row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),

                # 메인 컨테이너
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=360,   # 추가
                    controls=[
                        ft.Container(
                            width=200,
                            height=200,
                            bgcolor=ft.Colors.BLACK,
                            shape=ft.BoxShape.CIRCLE,
                            image=ft.DecorationImage(
                                src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201901/20/28017477-0365-4a43-b546-008b603da621.jpg",
                                fit=ft.ImageFit.COVER
                            ),
                        ),
                    ]
                ),

                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Container(
                                    content=ft.Text("섭취량"),
                                    padding=2,
                                    # alignment=ft.Alignment.CENTER,
                                    bgcolor=ft.Colors.AMBER_200,
                                    width=150,
                                    height=70,
                                    border_radius=10,
                                ),
                                ft.Container(
                                    content=ft.Text("음수량"),
                                    padding=2,
                                    # alignment=ft.Alignment.CENTER,
                                    bgcolor=ft.Colors.AMBER_200,
                                    width=150,
                                    height=70,
                                    border_radius=10,
                                ),
                            ],
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                "기록요약",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0)
                                ),
                            ),
                                padding=2,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=300,
                                height=50,
                                border_radius=10,
                            ),

                    ]
                ),
                
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=360,   # 추가
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "밥주기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),
                                            
                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "약먹기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    margin = 10,
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),

                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "물주기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,  # 추가
                                        spacing=8,   # 추가
                                    ),

                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "밥주기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),
                                            
                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "약먹기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    margin = 10,
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),

                                            ft.Container(
                                                ft.ElevatedButton(
                                                    "물주기",
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=0)
                                                    ),
                                                ),
                                                    padding=2,
                                                    # alignment=ft.Alignment.CENTER,
                                                    # bgcolor=ft.Colors.AMBER_200,
                                                    width=70,
                                                    height=60,
                                                    border_radius=10,
                                                ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,  # 추가
                                        spacing=8,   # 추가
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
                            )
                        ),
                    ]
                ),

                # 하단 네이게이션 바
                nav()
            ],
            spacing=15,
        )
    )


if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)