from viewforge.core import App
from viewforge.ui.elements import Text
from viewforge.ui.layout import Stack
from viewforge.ui.links import RouteLinkButton
from viewforge.routing import RouterView, route

@route("/", "Home")
def home_view(params, route):
    return Text("\U0001F3E0 Welcome to the Home Page")


@route("/about", "About")
def about_view(params, route):
    return Text("\u2139\ufe0f About this app")


@route("/user/<id>", "User Profile")
def user_profile_view(params, route):
    user_id = params.get("id", "unknown")
    return Text(f"\U0001F464 Viewing user: {user_id}")


@route("/admin", "Admin Page")
def admin_view(params, route):
    return Stack([
        Text(route.meta("title")),
        RouteLinkButton(label="Admin Logs", to="/admin/logs")
    ])


@route("/admin/logs", "Admin Logs")
def admin_logs_view(params, route):
    return Stack([
        Text("\U0001F4DC Admin Logs")
    ])


@route("/search", "Search")
def search_view(params, route):
    term = route.query().get("term", "")
    return Text(f"🔍 Search results for: {term or '[nothing]'}")


# Layout

def build():
    return [
        Stack([
            RouteLinkButton(label="Home", to="/"),
            RouteLinkButton(label="About", to="/about"),
            RouteLinkButton(label="User 42", to="/user/42"),
            RouteLinkButton(label="Admin", to="/admin"),
            RouteLinkButton(label="Search for Apple", to="/search?term=apple"),
            RouterView()
        ], css={"gap": "1rem", "padding": "2rem"})
    ]


if __name__ == "__main__":
    App().run(build)
