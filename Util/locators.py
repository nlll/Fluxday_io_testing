locators_home_page = {'loc_departments': 'Departments',
                      'loc_team': 'Team',
                      'loc_users': 'Users',
                      'loc_reports': 'Reports',
                      'loc_oauth': 'OAuth applications',
                      'loc_search_field': 'search_keyword',
                      'loc_homepage_user': '//div[2]/div[1]/ul[3]/li[1]/a',
                      'home_page_title': '#pane2 div.pane2-meta div',
                      'loc_homepage_logo': 'h1 .app-logo'
                      }
locators_login_page = {'loc_login_user': '#user_email',
                       'loc_login_pass': '#user_password',
                       'loc_login_butt': '.btn-login',
                       'loc_login_title': '.app-logo-login'}

locators_oauth_page = {}

locators_team_page = {}

locators_users_page = {'add_user_button': '.dashed_link.transition',
                       'name_add_user': '#user_name',
                       'nickname_add_user': '#user_nickname',
                       'email_add_user': '#user_email',
                       'empl_code_add_user': '#user_employee_code',
                       'pass_add_user': '#user_password',
                       'pass_confirm_add_user': '#user_password_confirmation',
                       'user_page_title': 'div.title',
                       'save_button': '.button.alert.right',
                       'sett_user_button': '.icon.settings-link',
                       'del_user_butt': 'Delete',
                       'edit_user_butt': 'Edit',
                       'message': '.alert-box'}

locators_depart_page = {'loc_create_depart': 'Create department',
                        'loc_create_depart_title': '#project_name',
                        'loc_create_depart_code': '#project_code',
                        'loc_depart_title': '.main-title',
                        'loc_create_depart_save_btn': '.button.alert.right',
                        'loc_depart_icon_settings': '.icon.settings-link',
                        'loc_depart_icon_settings_edit': 'Edit',
                        'loc_depart_icon_settings_delete': 'Delete',
                        'loc_depart_edit_description': '#project_description',
                        'loc_depart_description': '.description',
                        'loc_depart_edit_url': '#project_website',
                        'loc_depart_url': '.website'
                        }

locators_reports_page = {'loc_worklogs': "//a[contains(text(),'Worklogs')]",
                         'loc_worklogs_drop': '//h5/ul/li/a',
                         'loc_month': '#s2id_month',
                         'loc_type_month': 'elect2-drop .select2-search .select2-input',
                         'loc_year': "#s2id_month",
                         'loc_report_butt': '//div[5]/div/a/span',
                         'loc_calendar': 'report_date',
                         'loc_calendar_next': "button.xdsoft_next",
                         'loc_report_type': '#s2id_report_type',
                         'loc_report_chosen_type': 'a.select2-choice',
                         'loc_report_pdf': '//a[2]',
                         'loc_detailed_report': '//a[4]',
                         'loc_reports': '.report',
                         'loc_group_by_name': 'th.name.header'}
