from ..base_websocket import BaseWebsocket
from ..settings import PiecesSettings
from .._pieces_lib.pieces_os_client import UserProfile,UserApi
import threading
import json


class AuthWebsocket(BaseWebsocket):
	@property
	def url(self):
		return PiecesSettings.AUTH_WS_URL

	def on_message(self,ws, message):
		try:
			self.on_message_callback(UserProfile.from_json(message))
		except json.decoder.JSONDecodeError:
			self.on_message_callback(None) # User logged out!

	def on_error(self,ws,error):
		if type(error) == OSError: # Some issues with the dns so we need to warn the user the websocket is not running
			returned_user = UserApi(PiecesSettings.api_client).user_snapshot()
			self.on_message_callback(getattr(returned_user,"user",None))
		print(error)