#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The script is written in Python and uses the  univention.udm  module to interact with the UDM. The  univention.config_registry  module is used to access the UCR. 

The script consists of several functions:
- get_schools(): This function retrieves all schools from the LDAP directory.
- check_bilo_license_admin_group_exists(school): This function checks whether the group bilo_lizenzadmins-{school} already exists for the school.
- create_bilo_license_admin_group(school): This function creates the group bilo_lizenzadmins-{school} if it does not already exist.
- get_group_users(group_dn): This function retrieves the list of users in a specified group.
- add_user_to_bilo_license_admin_group(user_dn, group_dn): This function adds a specified user to the bilo_lizenzadmins-{school} group.

The main function retrieves all schools and checks whether the group bilo_lizenzadmins-{school} already exists for each school. If the group does not exist, it is created. Additionally, if the --add-school-admins option is specified, the script retrieves users from the school admins group and adds them to the corresponding bilo_lizenzadmins group if they are not already members.

Usage:
Step 1a: Execute the following command the create the bilo_lizenzadmins groups if necessary:
python3 create_license_admin_groups.py 

Step 1b: Execute the following command the create the bilo_lizenzadmins for one school only:
python3 create_license_admin_groups.py --school <School-ID>

Step 1c: Execute the following command the create the bilo_lizenzadmins groups and add the school_admins to the related groups:
python3 create_license_admin_groups.py --add-school-admins

Step 1d: Execute the following command the create the bilo_lizenzadmins group for one school and add the school_admins to the related group:
python3 create_license_admin_groups.py --school <School-ID> --add-school-admins

Step 2: Add users to the groups:
The next step is to add the users to the groups. This is a manual process and can be done using the UMC or the command line.

Step 3: You can rerun this script at any time. It will not remove groups or users from groups
"""

import re
from univention.udm import UDM
from univention.config_registry.backend import ConfigRegistry
from optparse import OptionParser

options = None
ucr = ConfigRegistry()
ucr.load()


def setup():
    parseOptions()


def parseOptions():
    global options
    parser = OptionParser()
    parser.add_option("-s","--school",dest="school",help="",default='all_schools')
    parser.add_option("--add-school-admins",dest="add_school_admins",help="Add school admins to bilo_lizenzadmins-group",action='store_true')

    (options, args) = parser.parse_args()

def get_schools():
    udm_schools = UDM.admin().version(2).get('container/ou')
    schools     = udm_schools.search("objectClass=ucsschoolOrganizationalUnit", base=ucr['ldap/base'])
    
    school_short_name_list = []

    for school in schools:
        school_short_name_list.append(school.props.name)

    return school_short_name_list

def check_bilo_license_admin_group_exists(school):
    udm_groups = UDM.admin().version(2).get('groups/group')
    try:
        group = udm_groups.get(f"cn=bilo_lizenzadmins-{school},cn=groups,ou={school},{ucr['ldap/base']}")
        return True
    except:
        return False

def create_bilo_license_admin_group(school):
    school = school.lower()
    udm_groups = UDM.admin().version(2).get('groups/group')

    group = udm_groups.new()
    group.props.name = f"bilo_lizenzadmins-{school}"
    group.props.description = f"BILDUNGSLOGIN Lizenzadministratoren"
    group.position = f"cn=groups,ou={school},{ucr['ldap/base']}"
    group.save()
    
    print(f"Created group {group.dn}")

def get_group_users(group_dn):
    udm_groups = UDM.admin().version(2).get('groups/group')
    group      = udm_groups.get(group_dn)
    users = []
    for user in group.props.users:
        users.append(user)
    return users

def add_user_to_bilo_license_admin_group(user_dn, group_dn):
    udm_groups = UDM.admin().version(2).get('groups/group')
    group      = udm_groups.get(group_dn)
    group.props.users.append(user_dn)
    group.save()
    print(f"Added user {user_dn} to group {group_dn}")

def main():

    setup()

    if options.school == 'all_schools':
        schools = get_schools()
    else:
        schools = [options.school]

    for school in schools:
        print(school)
        if not check_bilo_license_admin_group_exists(school):
            create_bilo_license_admin_group(school)

        if options.add_school_admins:
            dn_group_school_admins  = f"cn=admins-{school},cn=ouadmins,cn=groups,{ucr['ldap/base']}"
            dn_group_license_admins = f"cn=bilo_lizenzadmins-{school},cn=groups,ou={school},{ucr['ldap/base']}"
            users_school_admin      = get_group_users(dn_group_school_admins)
            users_license_admin     = get_group_users(dn_group_license_admins) 
            
            for ua in users_school_admin:
                if ua not in users_license_admin:
                    add_user_to_bilo_license_admin_group(ua, dn_group_license_admins)

main()
