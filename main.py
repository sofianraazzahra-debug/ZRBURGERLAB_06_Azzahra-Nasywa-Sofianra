
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

KV = r"""
#:import dp kivy.metrics.dp

<PrimaryButton@Button>:
    background_normal: ""
    background_color: 0.37, 0.16, 0.95, 1
    color: 1, 1, 1, 1
    font_size: "14sp"
    bold: True
    size_hint_y: None
    height: dp(46)

<SecondaryButton@Button>:
    background_normal: ""
    background_color: 0.94, 0.92, 1, 1
    color: 0.37, 0.16, 0.95, 1
    font_size: "13sp"
    bold: True
    size_hint_y: None
    height: dp(44)

<NavButton@Button>:
    background_normal: ""
    background_color: 0.96, 0.95, 0.99, 1
    color: 0.30, 0.16, 0.60, 1
    font_size: "11sp"

<Header>:
    size_hint_y: None
    height: dp(50)
    Label:
        text: root.title
        color: 0.08, 0.08, 0.10, 1
        font_size: "22sp"
        bold: True
        halign: "left"
        text_size: self.size
    Button:
        text: "🛒"
        background_normal: ""
        background_color: 0,0,0,0
        font_size: "21sp"
        color: 0.37,0.16,0.95,1
        size_hint_x: None
        width: dp(48)
        on_release: app.go("cart")

<BottomNav@BoxLayout>:
    size_hint_y: None
    height: dp(62)
    spacing: dp(4)
    padding: dp(4)

<SignupScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(25)
        spacing: dp(12)
        Widget:
        Label:
            text: "🍔"
            font_size: "65sp"
            size_hint_y: None
            height: dp(85)
        Label:
            text: "ZR BURGER LAB"
            font_size: "27sp"
            bold: True
            color: 0.08,0.08,0.10,1
            size_hint_y: None
            height: dp(42)
        Label:
            text: "Daftar dan mulai pesan burger favoritmu."
            color: 0.42,0.42,0.47,1
            font_size: "13sp"
            size_hint_y: None
            height: dp(30)
        TextInput:
            hint_text: "Nama lengkap"
            multiline: False
            size_hint_y: None
            height: dp(46)
        TextInput:
            hint_text: "Email"
            multiline: False
            size_hint_y: None
            height: dp(46)
        TextInput:
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: dp(46)
        PrimaryButton:
            text: "Daftar"
            on_release: app.signup()
        SecondaryButton:
            text: "Sudah punya akun? Masuk"
            on_release: app.go("home")
        Widget:

<Header>:
    title: ""

<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18), dp(12), dp(18), dp(6)
        spacing: dp(10)
        Header:
            title: "Beranda"
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
                Label:
                    text: "Halo, Burger Lovers! 👋"
                    color: 0.08,0.08,0.10,1
                    font_size: "18sp"
                    bold: True
                    halign: "left"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(30)
                BoxLayout:
                    orientation: "vertical"
                    padding: dp(16)
                    spacing: dp(6)
                    size_hint_y: None
                    height: dp(145)
                    canvas.before:
                        Color:
                            rgba: 0.37,0.16,0.95,1
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [18,18,18,18]
                    Label:
                        text: "Burger Premium\\nKhusus Buat Kamu"
                        color: 1,1,1,1
                        font_size: "21sp"
                        bold: True
                        halign: "left"
                        text_size: self.size
                    Label:
                        text: "Diskon hingga 20% untuk menu pilihan hari ini."
                        color: 0.92,0.89,1,1
                        font_size: "12sp"
                        halign: "left"
                        text_size: self.size
                    PrimaryButton:
                        text: "Lihat Menu"
                        background_color: 1,1,1,1
                        color: 0.37,0.16,0.95,1
                        on_release: app.go("menu")
                Label:
                    text: "Menu Favorit"
                    color: 0.08,0.08,0.10,1
                    font_size: "20sp"
                    bold: True
                    halign: "left"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(32)
                GridLayout:
                    cols: 2
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(210)
                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(8)
                        spacing: dp(4)
                        canvas.before:
                            Color:
                                rgba: 0.97,0.95,1,1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [15,15,15,15]
                        Label:
                            text: "🍔"
                            font_size: "48sp"
                        Label:
                            text: "Truffle Wagyu"
                            bold: True
                            color: 0.08,0.08,0.10,1
                        Label:
                            text: "Rp 45.000"
                            color: 0.37,0.16,0.95,1
                            bold: True
                        SecondaryButton:
                            text: "Detail"
                            on_release: app.open_detail("Truffle Wagyu Burger", 45000)
                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(8)
                        spacing: dp(4)
                        canvas.before:
                            Color:
                                rgba: 0.97,0.95,1,1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [15,15,15,15]
                        Label:
                            text: "🍔"
                            font_size: "48sp"
                        Label:
                            text: "Classic Beef"
                            bold: True
                            color: 0.08,0.08,0.10,1
                        Label:
                            text: "Rp 32.000"
                            color: 0.37,0.16,0.95,1
                            bold: True
                        SecondaryButton:
                            text: "Detail"
                            on_release: app.open_detail("Classic Beef Burger", 32000)
        BottomNav:
            NavButton:
                text: "⌂\\nBeranda"
                on_release: app.go("home")
            NavButton:
                text: "☰\\nMenu"
                on_release: app.go("menu")
            NavButton:
                text: "♡\\nTentang"
                on_release: app.go("about")
            NavButton:
                text: "☎\\nKontak"
                on_release: app.go("contact")

<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18), dp(12), dp(18), dp(6)
        spacing: dp(10)
        Header:
            title: "Menu Listing"
        TextInput:
            hint_text: "Cari menu burger..."
            multiline: False
            size_hint_y: None
            height: dp(44)
        ScrollView:
            do_scroll_x: False
            GridLayout:
                cols: 2
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                ProductCard:
                    name: "Truffle Wagyu Burger"
                    price: 45000
                    emoji: "🍔"
                ProductCard:
                    name: "Classic Beef Burger"
                    price: 32000
                    emoji: "🍔"
                ProductCard:
                    name: "Chicken Crispy Burger"
                    price: 29000
                    emoji: "🍗"
                ProductCard:
                    name: "Smoky BBQ Burger"
                    price: 35000
                    emoji: "🥓"
        BottomNav:
            NavButton:
                text: "⌂\\nBeranda"
                on_release: app.go("home")
            NavButton:
                text: "☰\\nMenu"
                on_release: app.go("menu")
            NavButton:
                text: "♡\\nTentang"
                on_release: app.go("about")
            NavButton:
                text: "☎\\nKontak"
                on_release: app.go("contact")

<ProductCard>:
    orientation: "vertical"
    padding: dp(9)
    spacing: dp(4)
    size_hint_y: None
    height: dp(205)
    canvas.before:
        Color:
            rgba: 0.97,0.95,1,1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,15,15,15]
    Label:
        text: root.emoji
        font_size: "45sp"
    Label:
        text: root.name
        color: 0.08,0.08,0.10,1
        bold: True
        font_size: "12sp"
    Label:
        text: "Rp " + "{:,}".format(root.price).replace(",", ".")
        color: 0.37,0.16,0.95,1
        bold: True
    SecondaryButton:
        text: "Pilih"
        on_release: app.open_detail(root.name, root.price)

<DetailScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(10)
        Header:
            title: "Detail Menu"
        Label:
            text: "🍔"
            font_size: "100sp"
            size_hint_y: None
            height: dp(145)
        Label:
            text: root.product_name
            color: 0.08,0.08,0.10,1
            font_size: "21sp"
            bold: True
            size_hint_y: None
            height: dp(36)
        Label:
            text: root.description
            color: 0.40,0.40,0.45,1
            font_size: "13sp"
            halign: "left"
            valign: "top"
            text_size: self.size
        Label:
            text: "Rp " + "{:,}".format(root.price).replace(",", ".")
            color: 0.37,0.16,0.95,1
            font_size: "22sp"
            bold: True
            size_hint_y: None
            height: dp(40)
        Widget:
        PrimaryButton:
            text: "Tambah ke Keranjang"
            on_release: app.add_to_cart()
        SecondaryButton:
            text: "Kembali ke Menu"
            on_release: app.go("menu")

<CartScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(10)
        Header:
            title: "Keranjang"
        ScrollView:
            do_scroll_x: False
            Label:
                text: root.cart_text
                color: 0.18,0.18,0.20,1
                font_size: "14sp"
                halign: "left"
                valign: "top"
                text_size: self.width, None
                size_hint_y: None
                height: max(dp(100), self.texture_size[1])
        BoxLayout:
            size_hint_y: None
            height: dp(45)
            Label:
                text: "Total"
                bold: True
                color: 0.15,0.15,0.18,1
            Label:
                text: "Rp " + "{:,}".format(root.total).replace(",", ".")
                bold: True
                color: 0.37,0.16,0.95,1
        PrimaryButton:
            text: "Lanjut Checkout"
            disabled: root.total <= 0
            on_release: app.go("checkout")
        SecondaryButton:
            text: "Kembali ke Menu"
            on_release: app.go("menu")

<CheckoutScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(10)
        Header:
            title: "Checkout"
        Label:
            text: "Informasi Pemesan"
            bold: True
            color: 0.10,0.10,0.12,1
            halign: "left"
            text_size: self.size
            size_hint_y: None
            height: dp(28)
        TextInput:
            hint_text: "Nama lengkap"
            multiline: False
            size_hint_y: None
            height: dp(44)
        TextInput:
            hint_text: "Nomor WhatsApp"
            multiline: False
            size_hint_y: None
            height: dp(44)
        TextInput:
            hint_text: "Alamat pengantaran"
            size_hint_y: None
            height: dp(75)
        Label:
            text: "Metode Pembayaran"
            bold: True
            color: 0.10,0.10,0.12,1
            halign: "left"
            text_size: self.size
            size_hint_y: None
            height: dp(28)
        Spinner:
            text: "QRIS"
            values: ["QRIS", "Transfer Bank", "COD"]
            size_hint_y: None
            height: dp(44)
        Widget:
        PrimaryButton:
            text: "Bayar Sekarang"
            on_release: app.pay()

<PaymentScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(25)
        spacing: dp(12)
        Widget:
        Label:
            text: "✓"
            font_size: "72sp"
            color: 0.37,0.16,0.95,1
            size_hint_y: None
            height: dp(90)
        Label:
            text: "Pesanan Berhasil!"
            font_size: "25sp"
            bold: True
            color: 0.08,0.08,0.10,1
            size_hint_y: None
            height: dp(42)
        Label:
            text: "Pesanan kamu berhasil dibuat dan sedang diproses."
            color: 0.40,0.40,0.45,1
            font_size: "13sp"
            halign: "center"
            text_size: self.size
        Widget:
        PrimaryButton:
            text: "Kembali ke Beranda"
            on_release: app.go("home")

<AboutScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(10)
        Header:
            title: "Tentang Kami"
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                spacing: dp(10)
                size_hint_y: None
                height: dp(430)
                Label:
                    text: "Cerita Kami"
                    font_size: "21sp"
                    bold: True
                    color: 0.08,0.08,0.10,1
                    size_hint_y: None
                    height: dp(35)
                Label:
                    text: "ZR Burger Lab hadir untuk membuat burger premium yang tetap nyaman di kantong. Kami mengutamakan bahan segar, rasa konsisten, dan pengalaman pemesanan yang sederhana."
                    color: 0.35,0.35,0.40,1
                    font_size: "13sp"
                    halign: "left"
                    valign: "top"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(115)
                Label:
                    text: "Misi Kami"
                    font_size: "21sp"
                    bold: True
                    color: 0.08,0.08,0.10,1
                    size_hint_y: None
                    height: dp(35)
                Label:
                    text: "🍔 Bahan berkualitas\\n⭐ Rasa konsisten\\n💜 Pelayanan ramah"
                    color: 0.35,0.35,0.40,1
                    font_size: "14sp"
                    halign: "left"
                    text_size: self.size
        BottomNav:
            NavButton:
                text: "⌂\\nBeranda"
                on_release: app.go("home")
            NavButton:
                text: "☰\\nMenu"
                on_release: app.go("menu")
            NavButton:
                text: "♡\\nTentang"
                on_release: app.go("about")
            NavButton:
                text: "☎\\nKontak"
                on_release: app.go("contact")

<ContactScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(10)
        Header:
            title: "Kontak"
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                spacing: dp(10)
                size_hint_y: None
                height: dp(390)
                Label:
                    text: "Hubungi Kami"
                    font_size: "21sp"
                    bold: True
                    color: 0.08,0.08,0.10,1
                    size_hint_y: None
                    height: dp(38)
                Label:
                    text: "📱 WhatsApp\\n0812-3456-7890\\n\\n📧 Email\\nhello@zrburgerlab.com\\n\\n📍 Lokasi\\nMalang, Jawa Timur"
                    color: 0.30,0.30,0.34,1
                    font_size: "14sp"
                    halign: "left"
                    valign: "top"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(220)
                PrimaryButton:
                    text: "Chat WhatsApp"
                    on_release: app.contact_message()
        BottomNav:
            NavButton:
                text: "⌂\\nBeranda"
                on_release: app.go("home")
            NavButton:
                text: "☰\\nMenu"
                on_release: app.go("menu")
            NavButton:
                text: "♡\\nTentang"
                on_release: app.go("about")
            NavButton:
                text: "☎\\nKontak"
                on_release: app.go("contact")
"""

class Header(Screen):
    title = StringProperty("")

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class DetailScreen(Screen):
    product_name = StringProperty("Detail Menu")
    price = NumericProperty(0)
    description = StringProperty(
        "Burger lezat dengan bahan pilihan dan saus spesial ZR Burger Lab."
    )

class CartScreen(Screen):
    cart_text = StringProperty("Keranjang masih kosong.")
    total = NumericProperty(0)

class CheckoutScreen(Screen):
    pass

class PaymentScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

from kivy.uix.boxlayout import BoxLayout

class ProductCard(BoxLayout):
    # Product cards are ordinary widgets with explicit Kivy properties.
    # This avoids the AttributeError that occurred when KV evaluated root.price.
    name = StringProperty("")
    price = NumericProperty(0)
    emoji = StringProperty("🍔")

class ZRBurgerApp(App):
    cart = []
    current_product = None

    def build(self):
        Builder.load_string(KV)

        sm = ScreenManager(transition=FadeTransition(duration=0.15))

        # 9 halaman sesuai urutan desain Figma
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(DetailScreen(name="detail"))
        sm.add_widget(CartScreen(name="cart"))
        sm.add_widget(CheckoutScreen(name="checkout"))
        sm.add_widget(PaymentScreen(name="payment"))
        sm.add_widget(AboutScreen(name="about"))
        sm.add_widget(ContactScreen(name="contact"))

        return sm

    def on_start(self):
        # Halaman pertama sekarang DAFTAR/SIGN UP, bukan splash.
        self.go("signup")

    def go(self, screen_name):
        self.root.current = screen_name
        if screen_name == "cart":
            self.refresh_cart()

    def signup(self):
        # Event daftar untuk Tahap 1: cukup berpindah ke Home.
        self.go("home")

    def open_detail(self, name, price):
        self.current_product = (name, price)
        screen = self.root.get_screen("detail")
        screen.product_name = name
        screen.price = price
        self.go("detail")

    def add_to_cart(self):
        if self.current_product:
            self.cart.append(self.current_product)
        self.refresh_cart()
        self.go("cart")

    def refresh_cart(self):
        screen = self.root.get_screen("cart")

        if not self.cart:
            screen.cart_text = "Keranjang masih kosong."
            screen.total = 0
            return

        lines = []
        total = 0

        for i, (name, price) in enumerate(self.cart, 1):
            lines.append(
                f"{i}. {name}\n   Rp {price:,.0f}".replace(",", ".")
            )
            total += price

        screen.cart_text = "\n\n".join(lines)
        screen.total = total

    def pay(self):
        # Event pembayaran untuk Tahap 1.
        self.go("payment")

    def contact_message(self):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label

        Popup(
            title="ZR Burger Lab",
            content=Label(
                text="Terima kasih! Silakan hubungi kami melalui WhatsApp."
            ),
            size_hint=(0.8, 0.25)
        ).open()


if __name__ == "__main__":
    ZRBurgerApp().run()
