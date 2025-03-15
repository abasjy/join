from rubpy import Client, filters
from rubpy.types import Update


app = Client('h_o')

@app.on_message_updates(filters.is_private)
def list(m:Update):
  if m.text.startswith("link"):
    t =m.text.replace('link','').strip()
    a = app.join_group(t)
    m.reply("به گروه پیوستم")
    
    
app.run()
