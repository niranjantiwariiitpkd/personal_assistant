from app.core.intents import Intent
from app.skills.notes import create_note
from app.skills.search import search_notes
from app.skills.web import open_website, web_search
from app.skills.system import play_music
from app.skills.capabilities import list_capabilities

SKILL_REGISTRY = {
    Intent.CREATE_NOTE: create_note,
    Intent.SEARCH_NOTES: search_notes,
    Intent.OPEN_WEBSITE: open_website,
    Intent.WEB_SEARCH: web_search,
    Intent.PLAY_MUSIC: play_music,
    Intent.CAPABILITIES: list_capabilities,

}
