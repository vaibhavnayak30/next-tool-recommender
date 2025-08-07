tool_vocab = [
    "cut", "copy", "paste", "select", "delete", "undo", "redo",
    "bold", "italic", "underline", "strike_through", "font_size", "font_family", "text_color", "highlight",
    "align_left", "align_center", "align_right", "align_justify",
    "indent", "outdent", "bullet_list", "numbered_list", "line_spacing",
    "save", "save_as", "open", "new_document", "print", "export_pdf",
    "find", "replace", "find_and_replace_all",
    "insert_image", "insert_table", "insert_link", "insert_shape", "insert_chart", "insert_header", "insert_footer",
    "zoom_in", "zoom_out", "page_layout", "read_mode", "web_layout",
    "add_comment", "track_changes", "accept_change", "reject_change", "share_document",
    "format_painter", "spell_check", "grammar_check", "word_count", "toggle_ruler"
]

tool_descriptions = {
    "cut": "removes selected content and places it in the clipboard, typically followed by paste",
    "copy": "duplicates selected content to the clipboard without removing it, often followed by paste",
    "paste": "inserts content from the clipboard at the current cursor position or replaces selected content",
    "select": "highlights content (text, image, etc.) for further operation like cut, copy, delete, or formatting",
    "delete": "removes content permanently; can often be undone",
    "undo": "reverses the last action performed, crucial for correcting mistakes",
    "redo": "re-applies a previously undone action, moving forward in the action history",
    "bold": "applies bold formatting to selected text, making it stand out",
    "italic": "applies italic formatting to selected text, often for emphasis or titles",
    "underline": "applies an underline to selected text, commonly used for links or emphasis",
    "strike_through": "draws a line through the middle of the selected text",
    "font_size": "changes the size of the selected text",
    "font_family": "changes the typeface or style of the selected text (e.g., Arial, Times New Roman)",
    "text_color": "changes the color of the selected text",
    "highlight": "applies a colored background to the selected text, like using a highlighter pen",
    "align_left": "aligns selected text or objects to the left margin",
    "align_center": "centers selected text or objects horizontally on the page",
    "align_right": "aligns selected text or objects to the right margin",
    "align_justify": "aligns text to both the left and right margins, adding space between words as needed",
    "indent": "increases the indentation of selected paragraphs or list items",
    "outdent": "decreases the indentation of selected paragraphs or list items",
    "bullet_list": "converts selected text into an unordered list with bullet points",
    "numbered_list": "converts selected text into an ordered list with numbers",
    "line_spacing": "adjusts the amount of vertical space between lines of text in a paragraph",
    "save": "stores the current state of the document to a file on disk",
    "save_as": "saves the current document with a different name or location",
    "open": "opens an existing document from a file",
    "new_document": "creates a blank new document, usually starting a fresh project",
    "print": "sends the current document to a printer for a hard copy",
    "export_pdf": "saves the document in PDF format, commonly used for sharing final versions",
    "find": "opens a dialog to search for specific text within the document",
    "replace": "opens a dialog to find text and replace it with new text, often used after 'find'",
    "find_and_replace_all": "finds all occurrences of text and replaces them automatically",
    "insert_image": "adds an image from a file into the document",
    "insert_table": "adds a structured grid of rows and columns to the document",
    "insert_link": "creates a hyperlink to a web page or location within the document",
    "insert_shape": "adds a geometric shape like a square or circle",
    "insert_chart": "adds a data visualization from a spreadsheet or other source",
    "insert_header": "adds content to the top margin of a document, appearing on every page",
    "insert_footer": "adds content to the bottom margin of a document, appearing on every page",
    "zoom_in": "magnifies the view of the document, making content appear larger",
    "zoom_out": "reduces the magnification of the document, showing more content at once",
    "page_layout": "changes the view to show how the document will look when printed",
    "read_mode": "optimizes the view for reading, hiding toolbars and menus",
    "web_layout": "shows the document as a web page, without page breaks",
    "add_comment": "inserts a comment bubble attached to a specific piece of text, often for collaboration",
    "track_changes": "activates a mode where all edits are marked for review",
    "accept_change": "applies a tracked change permanently to the document",
    "reject_change": "discards a tracked change, restoring the original text",
    "share_document": "opens a dialog to share the document with other users for collaboration",
    "format_painter": "copies formatting from one piece of content and applies it to another",
    "spell_check": "initiates a check for spelling errors in the document",
    "grammar_check": "initiates a check for grammatical errors in the document",
    "word_count": "displays a count of words, characters, and pages in the document",
    "toggle_ruler": "shows or hides the horizontal and vertical rulers"
}

tool_patterns = {
    "cut": ["paste", "undo", "copy", "select", "save"],
    "copy": ["paste", "undo", "select", "cut"],
    "paste": ["undo", "select", "cut", "bold", "italic", "format_painter"],
    "select": ["cut", "copy", "delete", "bold", "italic", "underline", "align_left", "format_painter"],
    "delete": ["undo", "select", "cut", "save"],
    "undo": ["redo", "cut", "copy", "paste", "delete", "save"],
    "redo": ["undo", "paste", "select", "bold", "italic"],
    "bold": ["italic", "underline", "select", "align_left"],
    "italic": ["bold", "underline", "select", "align_center"],
    "underline": ["bold", "italic", "select", "align_right"],
    "save": ["open", "new_document", "print", "export_pdf"],
    "save_as": ["save", "open", "print", "share_document"],
    "open": ["new_document", "save"],
    "new_document": ["save", "open", "insert_table", "insert_image"],
    "print": ["save", "new_document", "page_layout"],
    "export_pdf": ["save", "share_document"],
    "find": ["replace", "copy", "delete", "find_and_replace_all"],
    "replace": ["find", "undo", "save"],
    "find_and_replace_all": ["undo", "save", "find"],
    "align_left": ["align_center", "align_right", "align_justify", "select", "indent"],
    "align_center": ["align_left", "align_right", "align_justify", "select"],
    "align_right": ["align_left", "align_center", "align_justify", "select"],
    "align_justify": ["align_left", "align_center", "align_right", "select"],
    "indent": ["outdent", "bullet_list", "numbered_list"],
    "outdent": ["indent", "bullet_list", "numbered_list"],
    "bullet_list": ["numbered_list", "indent", "outdent", "select"],
    "numbered_list": ["bullet_list", "indent", "outdent", "select"],
    "format_painter": ["select", "paste", "bold", "italic"],
    "text_color": ["highlight", "select", "bold"],
    "highlight": ["text_color", "select"],
    "insert_image": ["select", "cut", "copy", "delete"],
    "insert_table": ["select", "insert_link", "insert_chart"],
    "insert_link": ["select", "copy"],
    "insert_shape": ["select", "cut", "copy", "delete"],
    "insert_chart": ["insert_table", "select", "cut", "copy"],
    "insert_header": ["insert_footer", "page_layout", "insert_link"],
    "insert_footer": ["insert_header", "page_layout"],
    "zoom_in": ["zoom_out", "read_mode", "page_layout"],
    "zoom_out": ["zoom_in", "page_layout", "web_layout"],
    "read_mode": ["page_layout", "web_layout", "zoom_in"],
    "add_comment": ["share_document", "track_changes", "select"],
    "track_changes": ["accept_change", "reject_change", "add_comment", "share_document"],
    "accept_change": ["reject_change", "track_changes", "save"],
    "reject_change": ["accept_change", "track_changes"],
    "share_document": ["save", "add_comment", "export_pdf"],
    "spell_check": ["grammar_check", "undo", "save"],
    "grammar_check": ["spell_check", "undo", "save"],
    "word_count": ["save", "print"],
}

# ==== Common workflow patterns ====
common_workflows = [
    # A user starts a new document, titles it, saves it, and adds initial text formatting
    ["new_document", "save_as", "select", "bold", "font_size", "align_center", "insert_header", "save"],

    # The user opens a file, cuts a section, pastes it elsewhere, and then applies formatting
    ["open", "select", "cut", "paste", "select", "align_justify", "line_spacing", "save"],

    # A user creates a bulleted list, adds a sub-list, and then changes it to a numbered list
    ["select", "bullet_list", "indent", "numbered_list", "outdent", "save"],

    # The user performs a mass text replacement, then checks for errors before saving and exporting
    ["find_and_replace_all", "undo", "spell_check", "grammar_check", "word_count", "save", "export_pdf"],
    
    # A user opens a shared document, reviews changes, and adds a comment before sharing it again
    ["share_document", "track_changes", "accept_change", "reject_change", "add_comment", "save"],

    # The user inserts an image, adjusts its size, and then adds a formatted caption
    ["insert_image", "select", "zoom_out", "insert_link", "align_center", "save"],
    
    # The user copies a formatted section, pastes it, and then uses the format painter to apply the style to a new section
    ["select", "copy", "paste", "select", "format_painter", "paste", "undo", "save"],
    
    # A user saves a document, adjusts the page layout, zooms in to review, and then sends it to the printer
    ["save", "page_layout", "zoom_in", "zoom_out", "print"],

    ["insert_table", "select", "paste", "bold", "align_center", "insert_link", "save"],

    # The user focuses on document structure, adding headers and footers with a page layout change
    ["new_document", "page_layout", "insert_header", "insert_footer", "save_as", "print"],
    
    # A user performs a full review, correcting errors and checking word count before saving
    ["open", "find", "spell_check", "grammar_check", "word_count", "save", "export_pdf"],
    
    # The user inserts a chart, then adds an explanatory shape and text to highlight a point
    ["insert_chart", "insert_shape", "select", "add_comment", "save"],
    
    # The user formats a paragraph with a mix of tools before adjusting its indentation
    ["select", "text_color", "highlight", "underline", "align_justify", "indent", "outdent", "save"],
    
    # The user adjusts the zoom and switches between view modes to review the document for different purposes
    ["zoom_in", "zoom_out", "read_mode", "page_layout", "save"],
    
    # The user makes a series of changes, then decides to revert them using multiple undo actions
    ["cut", "paste", "bold", "delete", "undo", "undo", "undo", "save"],

    # A user selects text, formats it, and then repeatedly uses the format painter
    ["select", "bold", "italic", "format_painter", "select", "format_painter", "select", "save"],
    
    # A user saves a document, then uses 'save as' to create a new version for a different purpose
    ["open", "track_changes", "save", "save_as", "export_pdf"],
    
    # The user selects text, adds a link, then revisits the link or its surrounding text
    ["select", "insert_link", "select", "underline", "save"],
    
    # The user adjusts line spacing and text alignment for a paragraph
    ["select", "line_spacing", "align_justify", "indent", "save"],
    
    # A user begins a new project by inserting a header and a table, then saves the empty structure
    ["new_document", "insert_header", "insert_table", "save_as"],
    
    # The user is in review mode and selectively accepts and rejects changes
    ["track_changes", "accept_change", "accept_change", "reject_change", "accept_change", "save"],
    
    # The user checks the document at different zoom levels and in different layouts
    ["zoom_in", "page_layout", "zoom_out", "read_mode", "save"],
    
    # A user formats a section, then deletes it and uses undo to retrieve it.
    ["select", "bold", "italic", "delete", "undo", "redo", "save"],

    # The user finds a specific word, copies it, and pastes it elsewhere
    ["find", "copy", "paste", "save"],

    # The user opens a document and immediately exports it for sharing
    ["open", "export_pdf", "share_document"],

    # The user inserts a sequence of different visual elements and then saves
    ["new_document", "insert_image", "insert_shape", "insert_chart", "save"],
    

    # The user converts a bulleted list to a numbered list and adjusts indentation, then reverts part of it
    ["select", "bullet_list", "indent", "numbered_list", "undo", "save"],
    
    # The user corrects a typo with delete/undo and then applies basic formatting
    ["delete", "undo", "select", "bold", "save"],

    # The user adjusts line spacing and switches between different layouts to see the impact
    ["select", "line_spacing", "web_layout", "page_layout", "save"],
    
    # A simple but common sequence where a user makes a quick, isolated change
    ["select", "text_color", "save"],
    ["open", "select", "font_family", "bold", "italic", "underline", "save"],
    ["open", "find", "spell_check", "grammar_check", "save"],
    ["new_document", "insert_header", "insert_table", "insert_image", "save"],
    ["track_changes", "reject_change", "add_comment", "save"],
    ["open", "page_layout", "toggle_ruler", "print"],
    ["find_and_replace_all", "undo", "find", "replace", "save"],
    ["select", "bullet_list", "indent", "numbered_list", "save"],
    ["select", "insert_link", "text_color", "save"],
    ["insert_shape", "insert_image", "select", "align_center", "save"],
    ["open", "select", "copy", "new_document", "paste", "format_painter", "save"],
]

test_histories = [
    ["open", "select", "font_family"],
    ["open", "find", "spell_check"],
    ["new_document", "insert_header", "insert_table"],
    ["track_changes", "reject_change"],
    ["open", "page_layout", "toggle_ruler"],
    ["find_and_replace_all", "undo"],
    ["select", "bullet_list", "indent"],
    ["select", "insert_link"],
    ["insert_shape", "insert_image", "select"],
    ["open", "select", "copy"],
    ["open", "find", "replace", "save"],
    ["new_document", "insert_header", "insert_footer"],
    ["save_as", "export_pdf", "share_document"],
]