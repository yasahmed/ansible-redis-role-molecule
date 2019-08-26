import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_redis_installed(host):
    redis_package_name = _get_redis_package_name(host.system_info.distribution)
    redis_package = host.package(redis_package_name)
    assert redis_package.is_installed

def test_redis_service_started_enabled(host):
    redis_service_name = _get_redis_package_name(host.system_info.distribution)
    redis_service = host.service(redis_service_name)
    assert redis_service.is_running
    assert redis_service.is_enabled


def _get_redis_package_name(host_distro):
    return {
        "ubuntu": "redis-server",
        "centos": "redis"
    }.get(host_distro, "redis")
