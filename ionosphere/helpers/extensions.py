from ionosphere.compute import VirtualMachineExtension, VirtualMachineScaleSetExtension

WINDOWS_CUSTOM_SCRIPT_EXTENSION_VERSION = '1.9'
WINDOWS_CUSTOM_SCRIPT_EXTENSION_TYPE = 'CustomScriptExtension'
WINDOWS_CUSTOM_SCRIPT_EXTENSION_PUBLISHER = 'Microsoft.Compute'

LINUX_CUSTOM_SCRIPT_EXTENSION_VERSION = '2.0'
LINUX_CUSTOM_SCRIPT_EXTENSION_TYPE = 'CustomScript'
LINUX_CUSTOM_SCRIPT_EXTENSION_PUBLISHER = 'Microsoft.Azure.Extensions'


def create_linux_custom_script(template, vm, command_to_execute, script=None, file_uris=None, storage_account_name=None,
                               storage_account_key=None, protected_settings=True, tags=None):
    vm_extention = VirtualMachineExtension(vm.title + '/CustomScriptForLinux',
                                           template=template,
                                           publisher=LINUX_CUSTOM_SCRIPT_EXTENSION_PUBLISHER,
                                           type=LINUX_CUSTOM_SCRIPT_EXTENSION_TYPE,
                                           autoUpgradeMinorVersion=True,
                                           typeHandlerVersion=LINUX_CUSTOM_SCRIPT_EXTENSION_VERSION,
                                           dependsOn=vm)

    set_common_extension_values(vm_extention=vm_extention,
                                vm=vm,
                                command_to_execute=command_to_execute,
                                script=script,
                                file_uris=file_uris,
                                storage_account_name=storage_account_name,
                                storage_account_key=storage_account_key,
                                protected_settings=protected_settings,
                                tags=tags)

    return vm_extention


def create_windows_custom_script(template, vm, command_to_execute, script=None, file_uris=None, storage_account_name=None,
                                 storage_account_key=None, protected_settings=True, tags=None):
    vm_extention = VirtualMachineExtension(vm.title + '/CustomScriptForWindows',
                                           template=template,
                                           publisher=WINDOWS_CUSTOM_SCRIPT_EXTENSION_PUBLISHER,
                                           type=WINDOWS_CUSTOM_SCRIPT_EXTENSION_TYPE,
                                           autoUpgradeMinorVersion=True,
                                           typeHandlerVersion=WINDOWS_CUSTOM_SCRIPT_EXTENSION_VERSION,
                                           dependsOn=vm)

    set_common_extension_values(vm_extention=vm_extention,
                                vm=vm,
                                command_to_execute=command_to_execute,
                                script=script,
                                file_uris=file_uris,
                                storage_account_name=storage_account_name,
                                storage_account_key=storage_account_key,
                                protected_settings=protected_settings,
                                tags=tags)

    return vm_extention


def create_scale_set_linux_custom_script(name, command_to_execute, script=None, file_uris=None,
                                         storage_account_name=None,
                                         storage_account_key=None, protected_settings=True):
    vm_extention = VirtualMachineScaleSetExtension(name,
                                                   publisher=LINUX_CUSTOM_SCRIPT_EXTENSION_PUBLISHER,
                                                   type=LINUX_CUSTOM_SCRIPT_EXTENSION_TYPE,
                                                   autoUpgradeMinorVersion=True,
                                                   typeHandlerVersion=LINUX_CUSTOM_SCRIPT_EXTENSION_VERSION)

    set_common_extension_values(vm_extention=vm_extention,
                                command_to_execute=command_to_execute,
                                script=script,
                                file_uris=file_uris,
                                storage_account_name=storage_account_name,
                                storage_account_key=storage_account_key,
                                protected_settings=protected_settings)

    return vm_extention


def create_scale_set_windows_custom_script(name, command_to_execute, script=None, file_uris=None,
                                           storage_account_name=None,
                                           storage_account_key=None, protected_settings=True):
    vm_extention = VirtualMachineScaleSetExtension(name,
                                                   publisher=WINDOWS_CUSTOM_SCRIPT_EXTENSION_PUBLISHER,
                                                   type=WINDOWS_CUSTOM_SCRIPT_EXTENSION_TYPE,
                                                   autoUpgradeMinorVersion=True,
                                                   typeHandlerVersion=WINDOWS_CUSTOM_SCRIPT_EXTENSION_VERSION)

    set_common_extension_values(vm_extention=vm_extention,
                                command_to_execute=command_to_execute,
                                script=script,
                                file_uris=file_uris,
                                storage_account_name=storage_account_name,
                                storage_account_key=storage_account_key,
                                protected_settings=protected_settings)

    return vm_extention


def set_common_extension_values(vm_extention, command_to_execute, vm=None, script=None, file_uris=None,
                                storage_account_name=None, storage_account_key=None, protected_settings=True,
                                tags=None):
    if script and file_uris or (not script and not file_uris):
        raise ValueError("Must set either script or an array of file uris")

    settings = {'commandToExecute': command_to_execute}

    if script:
        settings['script'] = script

    if file_uris:
        if isinstance(file_uris, str):
            file_uris = [file_uris]
        settings['fileUris'] = file_uris

    if storage_account_key:
        settings['storageAccountKey'] = storage_account_key

    if storage_account_name:
        settings['storageAccountName'] = storage_account_name

    if tags:
        vm_extention.properties['tags'] = tags

    if protected_settings:
        vm_extention.properties['protectedSettings'] = settings
    else:
        vm_extention.properties['settings'] = settings

    if vm:
        vm_extention.with_depends_on(vm)
