# -*- coding: utf-8 -*-

dictionary = \
{
    'lang':                             u'en',
#admin fields
    'admin':                            u'Administrator',
    'catalogs':                         u'Catalogs',
    'journals':                         u'Journals',
    'tables':                           u'Tables',
    'reports':                          u'Reports',
    'details':                          u'Details',
    'id':                               u'Record ID',
    'deleted_flag':                     u'Deleted flag',
    'caption':                          u'Caption',
    'name':                             u'Name',
    'table_name':                       u'Table',
    'template':                         u'Report template',
    'report_module':                    u'Report module',
    'params_template':                  u'Params UI',
    'view_template':                    u'Report template',
    'visible':                          u'Visible',
    'client_module':                    u'Client module',
    'web_client_module':                u'WebClient module',
    'server_module':                    u'Server module',
    'report_module':                    u'Report module',
    'project':                          u'Project',
    'users':                            u'Users',
    'roles':                            u'Roles',
    'privileges':                       u'Privileges',
    'tasks':                            u'Task',
    'safe_mode':                        u'Safe mode',
    'language':                         u'Language',
    'author':                           u'Author',
    'interface':                        u'Interface',
    'db_type':                          u'DB type',
    'db_name':                          u'File name',
    'alias':                            u'Database',
    'data_type':                        u'Type',
    'filter_type':                      u'Filter type',
    'size':                             u'Size',
    'object':                           u'Lookup item',
    'object_field':                     u'Lookup field',
    'lookup_values':                    u'Lookup values',
    'master_field':                     u'Master field',
    'required':                         u'Required',
    'calculated':                       u'Calc.',
    'default':                          u'Default',
    'read_only':                        u'Read only',
    'alignment':                        u'Alignment',
    'active':                           u'Active',
    'date':                             u'Date',
    'role':                             u'Role',
    'info':                             u'Information',
    'item':                             u'Item',
    'can_view':                         u'Can view',
    'can_create':                       u'Can create',
    'can_edit':                         u'Can edit',
    'can_delete':                       u'Can delete',
    'fields':                           u'Fields',
    'field':                            u'Field',
    'filter':                           u'Filter',
    'filters':                          u'Filters',
    'index':                            u'Index',
    'index_name':                       u'Index name',
    'report_params':                    u'Report params',
    'error':                            u'Error',
#admin interface
    'db':                               u'Database',
    'export':                           u'Export',
    'import':                           u'Import',
    'viewing':                          u'View',
    'editing':                          u'Edit',
    'filters':                          u'Filters',
    'order':                            u'Order',
    'indices':                          u'Indices',
    'foreign_keys':                     u'Foreign keys',
    'select_all':                       u'Select all',
    'unselect_all':                     u'Unselect all',
    'project_params':                   u'Parameters',
    'project_locale':                   u'Locale',
    'reserved_word':                    u'The name is a reserved word',
#editor
    'case_sensitive':                   u'Case sensitive',
    'whole_words':                      u'Find whole words only',
    'in_task':                          u'In task',
    'text_not_found':                   u'Text was not found.\nWrap search and find again?',
    'text_changed':                     u'Module has been changed.\nDo you want to save it before closing?',
    'go_to_line':                       u'Go to line',
    'go_to':                            u'Go to',
    'line':                             u'Line',
#admin editors
    'caption_name':                     u'Name',
    'caption_word_wrap':                u'Wrap',
    'caption_expand':                   u'Exp.',
    'caption_edit':                     u'Edit',
    'caption_descening':                u'Desc.',
#admin messages
    'fill_task_attrubutes':             u'Fill in the caption, name and database type attributes.',
    'can_not_connect':                  u"Can't connect to the database. %s",
    'field_used_in_filters':            u"Can't delete the field %s.\n It's used in filter definitions:\n%s",
    'field_used_in_fields':             u"Can't delete the field %s.\n It's used in field definitions:\n%s",
    'field_used_in_indices':            u"Can't delete the field %s.\n It's used in index definitions:\n%s",
    'field_is_system':                  u"Can't delete the system field.",
    'detail_mess':                      u'%s - detail %s',
    'item_used_in_items':               u"Can't delete the item %s.\n It's used in item definitions:\n%s",
    'field_mess':                       u'%s - field %s',
    'item_used_in_fields':              u"Can't delete the item %s.\n It's used in field definitions:\n%s",
    'param_mess':                       u'%s - parameter %s',
    'item_used_in_params':              u"Can't delete the item %s.\n It's used in param definitions:\n%s",
    'invalid_name':                     u'the Name is invalid.',
    'invalid_field_name':               u'The field name is invalid.',
    'type_is_required':                 u'The field type is required.',
    'index_name_required':              u'The index name is required.',
    'index_fields_required':            u'There are no index fields is required.',
    'cant_delete_group':                u"Can't delete the group.",
    'object_field_required':            u'A lookup field is required',
    'no_tasks_ptoject':                 u'There are no tasks in the project.',
    'stop_server':                      u'Stop server',
#interface buttons and labels
    'yes':                              u'Yes',
    'no':                               u'No',
    'ok':                               u'OK',
    'cancel':                           u'Cancel',
    'delete':                           u'Delete',
    'new':                              u'New',
    'edit':                             u'Edit',
    'copy':                             u'Copy',
    'print':                            u'Print',
    'save':                             u'Save',
    'open':                             u'Open',
    'close':                            u'Close',
    'select':                           u'Select',
    'filter':                           u'Filter',
    'apply':                            u'Apply',
    'find':                             u'Find',
    'replace':                          u'Replace',
    'view':                             u'View',
    'log_in':                           u'Log in',
    'login':                            u'Login',
    'password':                         u'Password',
    'log_out':                          u'Log out',
#runtime messages
    'invalid_int':                      u'%s invalid value - must be an integer',
    'invalid_float':                    u'%s invalid value - must be a float',
    'invalid_cur':                      u'%s invalid value - must be a currency',
    'invalid_date':                     u'%s invalid value - must be a date',
    'invalid_bool':                     u'%s invalid value - must be a boolean',
    'invalid_value':                    u'%s invalid value',
    'value_required':                   u'a value is required',
    'invalid_length':                   u'Text exceeds the maximum allowed length - %d',
    'save_changes':                     u'Data has been modified. Do you want to save changes?',
    'apply_changes':                    u"Data changes has not been applied to the server. Do you want to apply changes?",
    'delete_record':                    u'Delete the record?',
    'server_request_error':             u'Server request error',
    'cant_delete_used_record':          u"Can't delete the record. It's being used.",
    'website_maintenance':              u"The server is temporarily unavailable.",
    'apply_changes':                    u"Changed version. Press F5 to apply the changes",
    'items_selected':                   u"selected: %d",
    'invalid_range':                    u'Invalid range',
    'range_from':                       u'from',
    'range_to':                         u'to',
#rights messages
    'cant_view':                        u'%s: you are not allowed to view',
    'cant_create':                      u'%s: you are not allowed to create',
    'cant_edit':                        u'%s: you are not allowed to edit',
    'cant_delete':                      u'%s: you are not allowed to delete',
#calendar
    'week_start':                        0,
    'days_min':                         [u'Su', u'Mo', u'Tu', u'We', u'Th', u'Fr', u'Sa', u'Su'],
    'months':                           [u'January', u'February', u'March', u'April', u'May', u'June', u'July', u'August', u'September', u'October', u'November', u'December'],
    'months_short':                     [u'Jan', u'Feb', u'Mar', u'Apr', u'May', u'Jun', u'Jul', u'Aug', u'Sep', u'Oct', u'Nov', u'Dec'],
#grid
    'page':                             u'Page',
    'of':                               u'of'
}
