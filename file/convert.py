def convert_txt_to_paragraphs(input_file):
    """
    将txt文件转换为带<br>的HTML段落
    input_file: txt文件路径
    """
    # 生成输出文件名（在原文件名后加上_formatted.html）
    output_file = f"{input_file.rsplit('.', 1)[0]}_formatted.html"
    
    # 读取txt内容并处理
    with open(input_file, 'r', encoding='utf-8') as infile:
        paragraphs = infile.read().split('\n\n')  # 按空行分割段落
    
    # 处理内容
    formatted_content = '<div>\n'
    for para in paragraphs:
        if para.strip():  # 忽略空段落
            html_para = para.strip().replace('\n', '<br>\n')  # 将换行替换为<br>
            formatted_content += f'<p>{html_para}</p>\n\n'
    formatted_content += '</div>'
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(formatted_content)
    
    print(f'已将 {input_file} 转换为 {output_file}')

# 使用示例
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        convert_txt_to_paragraphs(input_file)
    else:
        print('请提供txt文件路径，例如：python convert.py 造车练习.txt') 