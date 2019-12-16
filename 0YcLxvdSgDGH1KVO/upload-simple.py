from default import gen_name, os, put_file, settings
if __name__ == "__main__":
    while 1:
        source = put_file.path_unify(input())
        if source[-1] != '/':
            put_file.put_file(file_path=source, repo_name=settings.simple_repo_name,
                              remote_path_setting="16", remote_name_setting=-1, cdn_test=False)
        else:
            remote_path_setting = gen_name.simple_gen(16)
            file_list = os.listdir(source)
            for file_name in file_list:
                file_path = source + file_name
                put_file.put_file(file_path=file_path, repo_name=settings.simple_repo_name,
                                  remote_path_setting=remote_path_setting, remote_name_setting=-1, cdn_test=False
                                  )
        print("========== Finished. ==========")
