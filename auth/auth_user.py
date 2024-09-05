from .._pieces_lib.pieces_os_client import UserProfile
from ..settings import PiecesSettings
import sublime
from typing import Optional


CONNECTING_HTML = "<p>Cloud Status: <span style=color:yellow>•</span> Connecting</p>"
DISCONNECTED_HTML = "<p>Cloud Status: <span style=color:red>•</span> Disconnected</p>"
CONNECTED_HTML = "<p>Cloud Status: <span style=color:green>•</span> Connected</p>"


class AuthUser:
	user_profile = None # Cache the user

	@classmethod
	def create_new_phantom(cls,html):
		PiecesSettings.output_panel.erase_phantoms("auth_phantom") # Remove the old phantom
		PiecesSettings.output_panel.add_phantom("auth_phantom", 
			sublime.Region(0, 0), html, sublime.LAYOUT_INLINE)

	@classmethod
	def on_user_callback(cls,user:Optional[UserProfile]=None):
		PiecesSettings.api_client.user.on_user_callback(user)
		sublime.active_window().focus_view(PiecesSettings.output_panel)
		cls.user_profile = user
		if not user:
			cls.login_page()
		else:
			cls.logout_page(user.email,user.name,user.allocation)

	@classmethod
	def login_page(cls):
		phantom_content = '<a href="subl:pieces_login"><b>Connect to your account</b></a>'
		cls.create_new_phantom(phantom_content)
		

	@classmethod
	def logout_page(cls,email,username,allocation=None,connecting=False):
		allocation_html = ""
		if allocation:
			status = allocation.status.cloud
			if status == "PENDING":
				allocation_html = CONNECTING_HTML
			elif status == "RUNNING" and "SUCCEEDED":
				allocation_html = CONNECTED_HTML
			elif status == "FAILED":
				allocation_html = DISCONNECTED_HTML

			try:
				if allocation.urls.vanity.url:
					allocation_html += f"<p>Personal Domain: {allocation.urls.vanity.url}</p>"
			except AttributeError:
				pass
		else:
			if connecting:
				allocation_html = CONNECTING_HTML
			else:
				allocation_html = DISCONNECTED_HTML
		phantom_content = f"<p>Username: {username}</p><p>Email: {email}</p>{allocation_html}<a href='subl:pieces_logout'>Logout</a>"
		cls.create_new_phantom(phantom_content)
